var stats = {
    type: "GROUP",
name: "Global Information",
path: "",
pathFormatted: "missing-name-b06d1",
stats: {
    "name": "Global Information",
    "numberOfRequests": {
        "total": "42303",
        "ok": "18644",
        "ko": "23659"
    },
    "minResponseTime": {
        "total": "0",
        "ok": "2",
        "ko": "0"
    },
    "maxResponseTime": {
        "total": "60019",
        "ok": "56725",
        "ko": "60019"
    },
    "meanResponseTime": {
        "total": "6554",
        "ok": "3747",
        "ko": "8766"
    },
    "standardDeviation": {
        "total": "16387",
        "ok": "7301",
        "ko": "20666"
    },
    "percentiles1": {
        "total": "10",
        "ok": "849",
        "ko": "0"
    },
    "percentiles2": {
        "total": "1525",
        "ok": "3272",
        "ko": "0"
    },
    "percentiles3": {
        "total": "60001",
        "ok": "15463",
        "ko": "60001"
    },
    "percentiles4": {
        "total": "60002",
        "ok": "37006",
        "ko": "60002"
    },
    "group1": {
        "name": "t < 800 ms",
        "count": 9305,
        "percentage": 22
    },
    "group2": {
        "name": "800 ms < t < 1200 ms",
        "count": 1607,
        "percentage": 4
    },
    "group3": {
        "name": "t > 1200 ms",
        "count": 7732,
        "percentage": 18
    },
    "group4": {
        "name": "failed",
        "count": 23659,
        "percentage": 56
    },
    "meanNumberOfRequestsPerSecond": {
        "total": "358.018",
        "ok": "157.787",
        "ko": "200.23"
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
        "total": "42303",
        "ok": "18644",
        "ko": "23659"
    },
    "minResponseTime": {
        "total": "0",
        "ok": "2",
        "ko": "0"
    },
    "maxResponseTime": {
        "total": "60019",
        "ok": "56725",
        "ko": "60019"
    },
    "meanResponseTime": {
        "total": "6554",
        "ok": "3747",
        "ko": "8766"
    },
    "standardDeviation": {
        "total": "16387",
        "ok": "7301",
        "ko": "20666"
    },
    "percentiles1": {
        "total": "10",
        "ok": "920",
        "ko": "0"
    },
    "percentiles2": {
        "total": "1524",
        "ok": "3273",
        "ko": "0"
    },
    "percentiles3": {
        "total": "60001",
        "ok": "15463",
        "ko": "60001"
    },
    "percentiles4": {
        "total": "60002",
        "ok": "37006",
        "ko": "60002"
    },
    "group1": {
        "name": "t < 800 ms",
        "count": 9305,
        "percentage": 22
    },
    "group2": {
        "name": "800 ms < t < 1200 ms",
        "count": 1607,
        "percentage": 4
    },
    "group3": {
        "name": "t > 1200 ms",
        "count": 7732,
        "percentage": 18
    },
    "group4": {
        "name": "failed",
        "count": 23659,
        "percentage": 56
    },
    "meanNumberOfRequestsPerSecond": {
        "total": "358.018",
        "ok": "157.787",
        "ko": "200.23"
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
