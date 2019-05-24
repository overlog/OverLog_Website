<template>
  <div class="example">
    <apexchart width="500" height="320" type="bar" :options="chartOptions" :series="series"></apexchart>
  </div>
</template>

<script>
import { mapState } from "vuex";
import VueApexCharts from "vue-apexcharts";
export default {
  name: "BarExample",
  components: {
    apexchart: VueApexCharts
  },
  data: function() {
    return {
      chartOptions: {
        plotOptions: {
          bar: {
            horizontal: false
          }
        },
        xaxis: {
          categories: ["Error", "Warning", "Info"]
        }
      },
      series: [
        {
          name: "series-1",
          data: [30, 40, 45]
        }
      ]
    };
  },
  computed: {
    ...mapState(["token", "userID"])
  },
  mounted() {
    console.log("...");
    fetch("http://127.0.0.1:5000/logs/" + this.token + "?userID=" + this.userID)
      .then(res => {
        return res.json();
      })
      .then(res => {
        this.setnums(res);
      });
  },
  methods: {
    setnums(res) {
      var datas = [];
      var types = [];
      res.map(entry => {
        if (!types.includes(entry["type"])) {
          types.push(entry["type"]);
          datas.push(0);
        }
      });

      var len = Object.keys(res).length;
      console.log(res[0]["type"]);

      for (var j = 0; j < len; j++) {
        datas[types.indexOf(res[j]["type"])]++;
      }
      this.series = this.series = [
        {
          data: datas
        }
      ];

      this.chartOptions = {
        xaxis: {
          categories: types
        }
      };
    }
  }
};
</script>
