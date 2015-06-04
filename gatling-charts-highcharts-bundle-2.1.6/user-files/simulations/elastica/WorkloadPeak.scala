package elastica // 1

import io.gatling.core.Predef._ // 2
import io.gatling.http.Predef._
import scala.concurrent.duration._

class WorkloadPeak extends Simulation { // 3
  val lbURL = System.getProperty("lbURL")
  val httpConf = http // 4
    .baseURL(lbURL) // 5
    .acceptHeader("text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8") // 6
    .doNotTrackHeader("1")
    .acceptLanguageHeader("en-US,en;q=0.5")
    .acceptEncodingHeader("gzip, deflate")
    .userAgentHeader("Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0")

  val scn = scenario("WorkloadPeak") // 7
    .exec(http("request_1")  // 8
    .get("/")) // 9
    .pause(1) // 10

	val tpic=50 //temps du pic
  	val debMin=10 //dbit min
  	val debMax=150 //dbit max
  	val tcalme= 200 //temps de la periode de calme
  
  setUp( // 11
    scn.inject(
		//debut sous-pattern
	    constantUsersPerSec(debMin) during(tcalme seconds) randomized,
	    rampUsersPerSec(debMin) to debMax during(tpic/2 seconds) randomized,
	    rampUsersPerSec(debMax) to debMin during(tpic/2 seconds) randomized,
	    //fin sous-pattern
	    constantUsersPerSec(debMin) during(tcalme seconds) randomized,
	    rampUsersPerSec(debMin) to debMax during(tpic/2 seconds) randomized,
	    rampUsersPerSec(debMax) to debMin during(tpic/2 seconds) randomized,
	    
	    constantUsersPerSec(debMin) during(tcalme seconds) randomized,
	    rampUsersPerSec(debMin) to debMax during(tpic/2 seconds) randomized,
	    rampUsersPerSec(debMax) to debMin during(tpic/2 seconds) randomized
    ).protocols(httpConf) // 13 
  ) 
}
