<template>
  <mdb-card-body>
    <div style="display: block">
      <mdb-pie-chart :data="pieChartData" :options="pieChartOptions" :height="200"/>
    </div>
  </mdb-card-body>
</template>

<script>
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

  data() {
    return {
      pieChartData: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
        datasets: [
          {
            data: [300, 50, 100, 40, 120, 24, 52],
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
        setChart(res);
      });
  },
  methods: {
    setChart(res) {}
  }
};
</script>

