<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <body>
    <?php
	/* Get dimmer from file */
	$serviceLevel = doubleval(@file_get_contents("/tmp/serviceLevel"));
	header("X-Dimmer: $serviceLevel");
	$r = rand(0, 9999) / 10000;
	$withOptional = ($r < $serviceLevel);
	header("X-WithOptional: $withOptional");
	$r2 = rand(0, 9999) / 10000;
	$withOptional2 = ($r < $serviceLevel) && ($r2 < $serviceLevel);
	header("X-WithOptional2: $withOptional2");

// Display the nested comments
function display_follow_up($cid, $level, $display, $filter, $link, $comment_table)
{
  $follow = mysql_query("SELECT story_id,id,subject,writer,date FROM $comment_table WHERE parent=$cid", $link) or die("ERROR: Query failed");
  while ($follow_row = mysql_fetch_array($follow))
  {
    for ($i = 0 ; $i < $level ; $i++)
      printf("&nbsp&nbsp&nbsp");
    print("<a href=\"/PHP/ViewComment.php?comment_table=$comment_table&storyId=".$follow_row["story_id"]."&commentId=".$follow_row["id"]."&filter=$filter&display=$display\">".$follow_row["subject"]."</a> by ".getUserName($follow_row["writer"], $link)." on ".$follow_row["date"]."<br>\n");
    if ($follow_row["childs"] > 0)
      display_follow_up($follow_row["id"], $level+1, $display, $filter, $link, $comment_table);
  }
}

    $scriptName = "ViewStory.php";
    include("PHPprinter.php");
    $startTime = getMicroTime();

    if (!isset($storyId)) /* Allow ViewStory.php to be included from RandomStory.php */
      $storyId = $_REQUEST['storyId'];
    if ($storyId == null)
    {
      printError($scriptName, $startTime, "Viewing story", "You must provide a story identifier!<br>");
      exit();
    }

    getDatabaseLink($link);
    $result = mysql_query("SELECT * FROM stories WHERE id=$storyId") or die("ERROR: Query failed");
    if (mysql_num_rows($result) == 0)
    {
      $result = mysql_query("SELECT * FROM old_stories WHERE id=$storyId") or die("ERROR: Query failed");
      $comment_table = "old_comments";
    }
    else
      $comment_table = "comments";
    if (mysql_num_rows($result) == 0)
      die("<h3>ERROR: Sorry, but this story does not exist.</h3><br>\n");
    $row = mysql_fetch_array($result);
    $username = getUserName($row["writer"], $link);

    // Display the story
    printHTMLheader("RUBBoS: Viewing story ".$row["title"]);
    printHTMLHighlighted($row["title"]);
    print("Posted by ".$username." on ".$row["date"]."<br>\n");
    print($row["body"]."<br>\n");
      print("<p><center><a href=\"/PHP/PostComment.php?comment_table=$comment_table&storyId=$storyId&parent=0\">Post a comment on this story</a></center><p>");

	// NOTE: this code section has not been reindented, to minimize "diff" output.

      // Optional code 2: recommender system
      if ($withOptional2) {
        echo chr(129); // Special marker for httpmon

        // Due to bad optimizing in MySQL, we need to do this in two steps
        // Step 1: retrieve story IDs, ordered by popularity, top 5
        $recommenderIdsQuery =
          "SELECT ".
            "c2.story_id as id,".
            "count(c2.story_id) as popularity,".
            "c2.date as date ".
          "FROM ".
            "comments AS c ".
            "LEFT JOIN comments AS c2 ON (c.writer=c2.writer) ".
          "WHERE c.story_id=".$storyId. " AND c2.story_id!=".$storyId." ".
          "GROUP BY id ".
          "ORDER BY popularity DESC, date DESC LIMIT 5;" ;
        //echo $recommenderIdsQuery; // For debugging
        $recommenderIdsResult = mysql_query($recommenderIdsQuery, $link);
        $ids = array();
        while ($row = mysql_fetch_array($recommenderIdsResult))
          array_push($ids, $row["id"]);
        array_push($ids, 0); // Make sure at least one item is recommended
        mysql_free_result($recommenderIdsResult);

        // Step 2: get all information about the stories and display them
        $recommenderQuery = "SELECT * FROM stories WHERE id IN (" . join(",", $ids) . ")";
        //echo $recommenderQuery; // For debugging
        $recommenderResult = mysql_query($recommenderQuery, $link);

        // Display stories
        print("Similar stories: <br>");
        while ($row = mysql_fetch_array($recommenderResult))
        {
          print("<a href=\"/PHP/ViewStory.php?storyId=".$row['id']."\">".$row['title']."</a> | ");
        }
        mysql_free_result($recommenderResult);
      }

    // Optional code 1: comments
    if ($withOptional)
    {
      echo chr(128); // Special marker for httpmon

    // Display filter chooser header
    print("<br><hr><br>");
    print("<center><form action=\"/PHP/ViewComment.php\" method=POST>\n".
          "<input type=hidden name=commentId value=0>\n".
          "<input type=hidden name=storyId value=$storyId>\n".
          "<input type=hidden name=comment_table value=$comment_table>\n".
          "<B>Filter :</B>&nbsp&nbsp<SELECT name=filter>\n");
    $count_result = mysql_query("SELECT rating, COUNT(rating) AS count FROM $comment_table WHERE story_id=$storyId GROUP BY rating ORDER BY rating", $link) or die("ERROR: Query failed");
    $i = -1;
    while ($count_row = mysql_fetch_array($count_result))
    {
      while (($i < 6) && ($count_row["rating"] != $i))
      {
        if ($i == $filter)
          print("<OPTION selected value=\"$i\">$i: 0 comment</OPTION>\n");
        else
          print("<OPTION value=\"$i\">$i: 0 comment</OPTION>\n");
        $i++;
      }
      if ($count_row["rating"] == $i)
      {
        if ($i == $filter)
          print("<OPTION selected value=\"$i\">$i: ".$count_row["count"]." comments</OPTION>\n");
        else
          print("<OPTION value=\"$i\">$i: ".$count_row["count"]." comments</OPTION>\n");
        $i++;
      }
    }
    while ($i < 6)
    {
      print("<OPTION value=\"$i\">$i: 0 comment</OPTION>\n");
      $i++;
    }

    print("</SELECT>&nbsp&nbsp&nbsp&nbsp<SELECT name=display>\n".
          "<OPTION value=\"0\">Main threads</OPTION>\n".
          "<OPTION selected value=\"1\">Nested</OPTION>\n".
          "<OPTION value=\"2\">All comments</OPTION>\n".
          "</SELECT>&nbsp&nbsp&nbsp&nbsp<input type=submit value=\"Refresh display\"></center><p>\n");          
    $display = 1;
    $filter = 0;

    // Display the comments
    $comment = mysql_query("SELECT * FROM $comment_table WHERE story_id=$storyId AND parent=0 AND rating>=$filter", $link) or die("ERROR: Query failed");
    while ($comment_row = mysql_fetch_array($comment))
    {
      print("<br><hr><br>");
      $username = getUserName($comment_row["writer"], $link);
      print("<TABLE width=\"100%\" bgcolor=\"#CCCCFF\"><TR><TD><FONT size=\"4\" color=\"#000000\"><B><a href=\"/PHP/ViewComment.php?comment_table=$comment_table&storyId=$storyId&commentId=".$comment_row["id"]."&filter=$filter&display=$display\">".$comment_row["subject"]."</a></B>&nbsp</FONT> (Score:".$comment_row["rating"].")</TABLE>\n");
      print("<TABLE><TR><TD><B>Posted by ".$username." on ".$comment_row["date"]."</B><p>\n");
      print("<TR><TD>".$comment_row["comment"]);
      print("<TR><TD><p>[ <a href=\"/PHP/PostComment.php?comment_table=$comment_table&storyId=$storyId&parent=".$comment_row["id"]."\">Reply to this</a>&nbsp|&nbsp".
            "<a href=\"/PHP/ViewComment.php?comment_table=$comment_table&storyId=$storyId&commentId=".$comment_row["parent"]."&filter=$filter&display=$display\">Parent</a>".
            "&nbsp|&nbsp<a href=\"/PHP/ModerateComment.php?comment_table=$comment_table&commentId=".$comment_row["id"]."\">Moderate</a> ]</TABLE>\n");
      if ($comment_row["childs"] > 0)
        display_follow_up($comment_row[id], 1, $display, $filter, $link, $comment_table);
    }

    } /* end Optional code 1: comments */
    else
    {
      echo "Comments are temporarily disabled";
    }

    mysql_free_result($result);
    mysql_close($link);
    
    printHTMLfooter($scriptName, $startTime);
    ?>
  </body>
</html>
