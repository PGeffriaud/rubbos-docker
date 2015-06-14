var stats = {
    type: "GROUP",
name: "Global Information",
path: "",
pathFormatted: "missing-name-b06d1",
stats: {
    "name": "Global Information",
    "numberOfRequests": {
        "total": "42421",
        "ok": "42421",
        "ko": "0"
    },
    "minResponseTime": {
        "total": "2",
        "ok": "2",
        "ko": "-"
    },
    "maxResponseTime": {
        "total": "3382",
        "ok": "3382",
        "ko": "-"
    },
    "meanResponseTime": {
        "total": "157",
        "ok": "157",
        "ko": "-"
    },
    "standardDeviation": {
        "total": "346",
        "ok": "346",
        "ko": "-"
    },
    "percentiles1": {
        "total": "38",
        "ok": "38",
        "ko": "-"
    },
    "percentiles2": {
        "total": "179",
        "ok": "179",
        "ko": "-"
    },
    "percentiles3": {
        "total": "510",
        "ok": "510",
        "ko": "-"
    },
    "percentiles4": {
        "total": "1484",
        "ok": "1484",
        "ko": "-"
    },
    "group1": {
        "name": "t < 800 ms",
        "count": 40627,
        "percentage": 96
    },
    "group2": {
        "name": "800 ms < t < 1200 ms",
        "count": 759,
        "percentage": 2
    },
    "group3": {
        "name": "t > 1200 ms",
        "count": 1035,
        "percentage": 2
    },
    "group4": {
        "name": "failed",
        "count": 0,
        "percentage": 0
    },
    "meanNumberOfRequestsPerSecond": {
        "total": "664.188",
        "ok": "664.188",
        "ko": "-"
    }
},
contents: {
"request-1-46da4": {
        type: "REQUEST",
        name: "request_1",
path: "request_1",
pathFormatted: "request-1-46da4",
stats: {
    "name": "request_1",
    "numberOfRequests": {
        "total": "42421",
        "ok": "42421",
        "ko": "0"
    },
    "minResponseTime": {
        "total": "2",
        "ok": "2",
        "ko": "-"
    },
    "maxResponseTime": {
        "total": "3382",
        "ok": "3382",
        "ko": "-"
    },
    "meanResponseTime": {
        "total": "157",
        "ok": "157",
        "ko": "-"
    },
    "standardDeviation": {
        "total": "346",
        "ok": "346",
        "ko": "-"
    },
    "percentiles1": {
        "total": "38",
        "ok": "38",
        "ko": "-"
    },
    "percentiles2": {
        "total": "179",
        "ok": "179",
        "ko": "-"
    },
    "percentiles3": {
        "total": "510",
        "ok": "510",
        "ko": "-"
    },
    "percentiles4": {
        "total": "1484",
        "ok": "1484",
        "ko": "-"
    },
    "group1": {
        "name": "t < 800 ms",
        "count": 40627,
        "percentage": 96
    },
    "group2": {
        "name": "800 ms < t < 1200 ms",
        "count": 759,
        "percentage": 2
    },
    "group3": {
        "name": "t > 1200 ms",
        "count": 1035,
        "percentage": 2
    },
    "group4": {
        "name": "failed",
        "count": 0,
        "percentage": 0
    },
    "meanNumberOfRequestsPerSecond": {
        "total": "664.188",
        "ok": "664.188",
        "ko": "-"
    }
}
    }
}

}

function fillStats(stat){
    $("#numberOfRequests").append(stat.numberOfRequests.total);
    $("#numberOfRequestsOK").append(stat.numberOfRequests.ok);
    $("#numberOfRequestsKO").append(stat.numberOfRequests.ko);

    $("#minResponseTime").append(stat.minResponseTime.total);
    $("#minResponseTimeOK").append(stat.minResponseTime.ok);
    $("#minResponseTimeKO").append(stat.minResponseTime.ko);

    $("#maxResponseTime").append(stat.maxResponseTime.total);
    $("#maxResponseTimeOK").append(stat.maxResponseTime.ok);
    $("#maxResponseTimeKO").append(stat.maxResponseTime.ko);

    $("#meanResponseTime").append(stat.meanResponseTime.total);
    $("#meanResponseTimeOK").append(stat.meanResponseTime.ok);
    $("#meanResponseTimeKO").append(stat.meanResponseTime.ko);

    $("#standardDeviation").append(stat.standardDeviation.total);
    $("#standardDeviationOK").append(stat.standardDeviation.ok);
    $("#standardDeviationKO").append(stat.standardDeviation.ko);

    $("#percentiles1").append(stat.percentiles1.total);
    $("#percentiles1OK").append(stat.percentiles1.ok);
    $("#percentiles1KO").append(stat.percentiles1.ko);

    $("#percentiles2").append(stat.percentiles2.total);
    $("#percentiles2OK").append(stat.percentiles2.ok);
    $("#percentiles2KO").append(stat.percentiles2.ko);

    $("#percentiles3").append(stat.percentiles3.total);
    $("#percentiles3OK").append(stat.percentiles3.ok);
    $("#percentiles3KO").append(stat.percentiles3.ko);

    $("#percentiles4").append(stat.percentiles4.total);
    $("#percentiles4OK").append(stat.percentiles4.ok);
    $("#percentiles4KO").append(stat.percentiles4.ko);

    $("#meanNumberOfRequestsPerSecond").append(stat.meanNumberOfRequestsPerSecond.total);
    $("#meanNumberOfRequestsPerSecondOK").append(stat.meanNumberOfRequestsPerSecond.ok);
    $("#meanNumberOfRequestsPerSecondKO").append(stat.meanNumberOfRequestsPerSecond.ko);
}
