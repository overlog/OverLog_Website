<template>
  <div align="center" class="example">
    <mdb-btn-group>
      <mdb-btn v-if="xinterval=='1h'" @click="setXinterval('1h')" color="info" darkWaves>1H</mdb-btn>
      <mdb-btn @click="setXinterval('1h')" outline="mdb-color" v-else darkWaves>1H</mdb-btn>

      <mdb-btn v-if="xinterval=='1d'" @click="setXinterval('1d')" color="info" darkWaves>1D</mdb-btn>
      <mdb-btn @click="setXinterval('1d')" outline="mdb-color" v-else darkWaves>1D</mdb-btn>

      <mdb-btn v-if="xinterval=='1w'" @click="setXinterval('1w')" color="info" darkWaves>1W</mdb-btn>
      <mdb-btn v-else @click="setXinterval('1w')" outline="mdb-color" darkWaves>1W</mdb-btn>

      <mdb-btn v-if="xinterval=='1m'" @click="setXinterval('1m')" color="info" darkWaves>1M</mdb-btn>
      <mdb-btn v-else @click="setXinterval('1m')" outline="mdb-color" darkWaves>1M</mdb-btn>

      <mdb-btn v-if="xinterval=='3m'" @click="setXinterval('3m')" color="info" darkWaves>3M</mdb-btn>
      <mdb-btn v-else @click="setXinterval('3m')" outline="mdb-color" darkWaves>3M</mdb-btn>

      <mdb-btn v-if="xinterval=='6m'" @click="setXinterval('6m')" color="info" darkWaves>6M</mdb-btn>
      <mdb-btn v-else @click="setXinterval('6m')" outline="mdb-color" darkWaves>6M</mdb-btn>

      <mdb-btn v-if="xinterval=='1y'" @click="setXinterval('1y')" color="info" darkWaves>1Y</mdb-btn>
      <mdb-btn v-else @click="setXinterval('1y')" outline="mdb-color" darkWaves>1Y</mdb-btn>
    </mdb-btn-group>

    <select
      outline="mdb-color"
      @change="updateChart()"
      v-model="datainterval"
      class="browser-default custom-select"
    >
      <option value="1min" v-if="mins">1 Min</option>
      <option value="5min" v-if="mins">5 Mins</option>
      <option value="1h" v-if="h1">1 Hour</option>
      <option value="4h" v-if="h4">4 Hour</option>
      <option value="1d" v-if="d1">1 Day</option>
      <option value="1w" v-if="w1">1 Week</option>
      <option value="1m" v-if="m1">1 Month</option>
    </select>

    <br>
    <hr>
    <br>
    <apexchart width="90%" height="300" type="line" :options="chartOptions" :series="series"></apexchart>
  </div>
</template>

<script>
import { mapState } from "vuex";
import {
  mdbBtn,
  mdbBtnGroup,
  mdbDropdown,
  mdbDropdownItem,
  mdbDropdownMenu,
  mdbDropdownToggle,
  mdbSelect
} from "mdbvue";
import VueApexCharts from "vue-apexcharts";
import { log } from "util";
export default {
  name: "BarExample",
  components: {
    apexchart: VueApexCharts,
    mdbBtn,
    mdbBtnGroup,
    mdbDropdown,
    mdbDropdownItem,
    mdbDropdownMenu,
    mdbDropdownToggle,
    mdbSelect
  },
  data: function() {
    return {
      logs: {},
      datainterval: "1h",
      xinterval: "1d",
      chartOptions: {
        plotOptions: {
          bar: {
            horizontal: true
          }
        },
        xaxis: {
          categories: []
        }
      },
      series: [
        {
          name: "# of Log",
          data: []
        }
      ]
    };
  },
  computed: {
    mins: function() {
      if (this.xinterval == "1h") {
        return true;
      }
      return false;
    },

    h1: function() {
      if (this.xinterval == "1d") {
        return true;
      }
      return false;
    },
    h4: function() {
      if (this.xinterval == "1d") {
        return true;
      }
      return false;
    },
    d1: function() {
      if (
        this.xinterval == "1w" ||
        this.xinterval == "1m" ||
        this.xinterval == "3m"
      ) {
        return true;
      }
      return false;
    },
    w1: function() {
      if (
        this.xinterval == "1m" ||
        this.xinterval == "3m" ||
        this.xinterval == "6m" ||
        this.xinterval == "1y"
      ) {
        return true;
      }
      return false;
    },

    m1: function() {
      if (
        this.xinterval == "3m" ||
        this.xinterval == "6m" ||
        this.xinterval == "1y"
      ) {
        return true;
      }
      return false;
    },
    ...mapState(["token", "userID"])
  },

  mounted() {
    fetch("http://127.0.0.1:5000/logs/" + this.token + "?userID=" + this.userID)
      .then(res => {
        return res.json();
      })
      .then(res => {
        this.logs = res;
      });
  },
  methods: {
    setXinterval(str) {
      this.xinterval = str;

      if (this.xinterval == "1h") {
        this.datainterval = "5min";
      } else if (this.xinterval == "1d") {
        this.datainterval = "1h";
      } else if (this.xinterval == "1w") {
        this.datainterval = "1d";
      } else if (this.xinterval == "1m") {
        this.datainterval = "1w";
      } else if (this.xinterval == "3m") {
        this.datainterval = "1w";
      } else if (this.xinterval == "6m") {
        this.datainterval = "1m";
      } else if (this.xinterval == "1y") {
        this.datainterval = "1m";
      }

      this.updateChart();
    },

    setGraph(startDate, endDate, interval, logs) {
      var dates = [];
      var amounts = [];
      console.log(iterDate);

      console.log(startDate);
      console.log(endDate);
      var iterDate = startDate.getTime();
      while (iterDate < endDate.getTime()) {
        dates.push(new Date(iterDate));
        iterDate = iterDate + interval;
      }

      var datesIndex = 1;
      var num = 0;

      var counter = 0;
      for (let i = 0; i < Object.keys(logs).length; i++) {
        if (new Date(logs[i]["date"]).getTime() < dates[datesIndex].getTime()) {
          // console.log(dates[datesIndex]);
          // console.log("sdadas " + logs[i]["date"]);
          num++;
          counter++;
        } else {
          console.log("else " + logs[i]["date"]);
          console.log(dates[datesIndex]);
          console.log(num);
          amounts.push(num);
          num = 0;

          datesIndex++;
          // console.log(dates[datesIndex].getTime());

          while (
            new Date(logs[i]["date"]).getTime() > dates[datesIndex].getTime()
          ) {
            amounts.push(0);
            datesIndex++;
            // console.log(dates[datesIndex].getTime());
          }
          num++;
          counter++;
        }
      }
      console.log(counter);
      amounts.push(num);

      while (Object.keys(amounts).length < Object.keys(dates).length) {
        amounts.push(0);
      }

      console.log(dates);
      console.log(amounts);

      this.chartOptions = {
        xaxis: {
          categories: dates
        }
      };

      this.series = this.series = [
        {
          data: amounts
        }
      ];
    },

    updateChart() {
      var endDate = new Date();
      endDate = new Date(
        endDate.getTime() - endDate.getTimezoneOffset() * 60 * 1000
      );
      if (this.xinterval == "1h") {
        var substraction = 60 * 60 * 1000;
        var startDate = new Date(endDate - substraction);
      } else if (this.xinterval == "1d") {
        var substraction = 60 * 60 * 24 * 1000;
        var startDate = new Date(endDate - substraction);
      } else if (this.xinterval == "1w") {
        var substraction = 7 * 60 * 60 * 24 * 1000;
        var startDate = new Date(endDate - substraction);
      } else if (this.xinterval == "1m") {
        var substraction = 30 * 60 * 60 * 24 * 1000;
        var startDate = new Date(endDate - substraction);
      } else if (this.xinterval == "3m") {
        var substraction = 3 * 30 * 60 * 60 * 24 * 1000;
        var startDate = new Date(endDate - substraction);
      } else if (this.xinterval == "6m") {
        var substraction = 6 * 30 * 60 * 60 * 24 * 1000;
        var startDate = new Date(endDate - substraction);
      } else if (this.xinterval == "1y") {
        var substraction = 12 * 30 * 60 * 60 * 24 * 1000;
        var startDate = new Date(endDate - substraction);
      }

      if (this.datainterval == "1min") {
        var interval = 60 * 1000;
      } else if (this.datainterval == "5min") {
        var interval = 5 * 60 * 1000;
      } else if (this.datainterval == "1h") {
        var interval = 60 * 60 * 1000;
      } else if (this.datainterval == "4h") {
        var interval = 4 * 60 * 60 * 1000;
      } else if (this.datainterval == "1d") {
        var interval = 24 * 60 * 60 * 1000;
      } else if (this.datainterval == "1w") {
        var interval = 7 * 24 * 60 * 60 * 1000;
      } else if (this.datainterval == "1m") {
        var interval = 30 * 60 * 60 * 24 * 1000;
      }

      var graphLogs = [];
      var logs = this.logs;

      if (interval > 4 * 60 * 60 * 1000) {
        startDate = new Date(startDate.setHours(0, 0, 0, 0));
        endDate = new Date(endDate.setHours(24, 0, 0, 0));
      }

      logs.map(log => {
        if (
          new Date(log["date"]).getTime() > startDate.getTime() &&
          new Date(log["date"]).getTime() < endDate.getTime()
        ) {
          graphLogs.push(log);
        }
      });

      this.setGraph(startDate, endDate, interval, graphLogs);
    }
  }
};
</script>