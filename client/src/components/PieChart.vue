<template>
  <mdb-card-body>
    <div style="display: block">
      <mdb-pie-chart :data="pieChartData" :options="pieChartOptions" :height="320" />
    </div>
  </mdb-card-body>
</template>

<script>
import { mapState } from "vuex";
import {
  mdbRow,
  mdbCol,
  mdbBtn,
  mdbCard,
  mdbCardBody,
  mdbCardHeader,
  mdbCardText,
  mdbIcon,
  mdbTbl,
  mdbPieChart
} from "mdbvue";
import { type } from "os";
export default {
  name: "PieChart",
  components: {
    mdbRow,
    mdbCol,
    mdbBtn,
    mdbCard,
    mdbCardBody,
    mdbCardHeader,
    mdbCardText,
    mdbIcon,
    mdbTbl,
    mdbPieChart
  },

  computed: {
    ...mapState(["token", "userID"])
  },

  data() {
    return {
      pieChartData: {
        labels: [],
        datasets: [
          {
            data: [],
            backgroundColor: [
              "#F7464A",
              "#46BFBD",
              "#FDB45C",
              "#949FB1",
              "#4D5360",
              "#ac64ad"
            ],
            hoverBackgroundColor: [
              "#FF5A5E",
              "#5AD3D1",
              "#FFC870",
              "#A8B3C5",
              "#616774",
              "#da92db"
            ]
          }
        ]
      }
    };
  },

  mounted() {
    fetch("http://127.0.0.1:5000/logs/" + this.token + "?userID=" + this.userID)
      .then(res => {
        return res.json();
      })
      .then(res => {
        this.logs = res;
        console.log(res);
        this.setChart(res);
        console.log("asdasd");
      });
  },
  methods: {
    setChart(res) {
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

      this.pieChartData = {
        labels: types,
        datasets: [
          {
            data: datas,
                        backgroundColor: [
              "#F7464A",
              "#46BFBD",
              "#FDB45C",
              "#949FB1",
              "#4D5360",
              "#ac64ad"
            ],
            hoverBackgroundColor: [
              "#FF5A5E",
              "#5AD3D1",
              "#FFC870",
              "#A8B3C5",
              "#616774",
              "#da92db"
            ]
          }
        ]
      };
    }
  }
};
</script>

