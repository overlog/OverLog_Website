<template>
  <div class="dashboard">

    <section>
      <section class="mt-lg-5">
        <mdb-row>
          <card v-for="c in cardRes" :res="c" v-bind:key="c.id"></card>
        </mdb-row>
      </section>
      <section>
        <mdb-row class="mt-5">
          <mdb-col class="mb-5">
            <mdb-card>
              <mdb-card-header>Search Log</mdb-card-header>
              <mdb-card-body>
                <div style="display: block">
                  <search-log></search-log>
                </div>
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
        </mdb-row>
      </section>

      <div >
      <section >
        <mdb-row class="mt-5" >
          <mdb-col md="3" class="mb-4">
            <mdb-card class="mb-4">
              <mdb-card-header class="text-center">Pie chart</mdb-card-header>
              <pie-chart ></pie-chart>
            </mdb-card>
          </mdb-col>
 
          <mdb-col md="5" class="mb-4">
            <mdb-card-header>Bar Chart</mdb-card-header>
            <mdb-card>
              <mdb-card-body>
                <div style="display: block">
                  <box-plot></box-plot>
                </div>
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
        </mdb-row>
      </section>
      </div>

      <section>
        <mdb-row class="mt-5">
          <mdb-col>
            <mdb-card>
              <mdb-card-header>Line chart</mdb-card-header>
              <mdb-card-body>
                <div style="display: block">
                  <line-chart></line-chart>
                </div>
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
        </mdb-row>
      </section>
      <section>
        <mdb-row class="mt-5">
          <mdb-col>
            <mdb-card>
              <mdb-card-header>Alert Alarm</mdb-card-header>
              <mdb-card-body>
                <div style="display: block">
                  <alert-alarm></alert-alarm>
                </div>
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
        </mdb-row>
      </section>
    </section>
  </div>
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
  mdbBarChart,
  mdbPieChart,
  mdbLineChart,
  mdbRadarChart,
  mdbDoughnutChart,
  mdbListGroup,
  mdbListGroupItem,
  mdbBadge,
  mdbModal,
  mdbModalHeader,
  mdbModalTitle,
  mdbModalBody,
  mdbModalFooter,
  mdbMultiCarousel,
  mdbCarouselItem,
  mdbContainer,

  mdbCardImage,
  mdbCardTitle,

} from "mdbvue";
import { error } from "util";
export default {
  name: "Dashboard",
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
    mdbBarChart,
    mdbPieChart,
    mdbLineChart,
    mdbRadarChart,
    mdbDoughnutChart,
    mdbListGroup,
    mdbListGroupItem,
    mdbBadge,
    mdbModal,
    mdbModalHeader,
    mdbModalTitle,
    mdbModalBody,
    mdbModalFooter,
    mdbMultiCarousel,
    mdbCarouselItem,
    mdbContainer,
    mdbRow,
    mdbCol,
    mdbCard,
    mdbCardImage,
    mdbCardBody,
    mdbCardTitle,
    mdbCardText
 
  },
  data() {
    return {
      res: {},
      cardRes: [],
      error: 0,
      showFrameModalTop: false,
      showFrameModalBottom: false,
      showSideModalTopRight: false,
      showSideModalTopLeft: false,
      showSideModalBottomRight: false,
      showSideModalBottomLeft: false,
      showCentralModalSmall: false,
      showCentralModalMedium: false,
      showCentralModalLarge: false,
      showCentralModalFluid: false,
      showFluidModalRight: false,
      showFluidModalLeft: false,
      showFluidModalTop: false,
      showFluidModalBottom: false
    };
  },

  computed: {
    data() {
      return {
        columns: [],
        rows: []
      };
    },
    ...mapState(["token", "userID"])
  },

  mounted() {
    var url =
      "http://127.0.0.1:5000/logs/" + this.token + "?userID=" + this.userID;
    fetch(url)
      .then(res => res.json())
      .then(json => {
        this.res = json;
        this.cards(json);
      });
  },

  methods: {
    cards(res) {
      var types = [];
      var datas = [];
      res.map(entry => {
        if (!types.includes(entry["type"])) {
          types.push(entry["type"]);
          datas.push([]);
        }
      });

      var len = Object.keys(res).length;
      console.log(res[0]["type"]);

      for (var j = 0; j < len; j++) {
        datas[types.indexOf(res[j]["type"])].push(res[j]);
      }

      this.cardRes = datas;
    }
  },

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
  },
  pieChartOptions: {
    responsive: true,
    maintainAspectRatio: false
  },
  radarChartData: {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
    datasets: [
      {
        label: "#1",
        backgroundColor: "rgba(245, 74, 85, 0.5)",
        data: [65, 59, 80, 81, 56, 55, 40]
      },
      {
        label: "#2",
        backgroundColor: "rgba(90, 173, 246, 0.5)",
        data: [12, 42, 121, 56, 24, 12, 2]
      },
      {
        label: "#3",
        backgroundColor: "rgba(245, 192, 50, 0.5)",
        data: [2, 123, 154, 76, 54, 23, 5]
      }
    ]
  },
  radarChartOptions: {
    responsive: true,
    maintainAspectRatio: false
  }
};
</script>

<style scoped>
.cascading-admin-card {
  margin: 20px 0;
}
.cascading-admin-card .admin-up {
  margin-left: 4%;
  margin-right: 4%;
  margin-top: -20px;
}
.cascading-admin-card .admin-up .fas,
.cascading-admin-card .admin-up .far {
  box-shadow: 0 2px 9px 0 rgba(0, 0, 0, 0.2), 0 2px 13px 0 rgba(0, 0, 0, 0.19);
  padding: 1.7rem;
  font-size: 2rem;
  color: #fff;
  text-align: left;
  margin-right: 1rem;
  border-radius: 3px;
}
.cascading-admin-card .admin-up .data {
  float: right;
  margin-top: 2rem;
  text-align: right;
}
.admin-up .data p {
  color: #999999;
  font-size: 12px;
}
.classic-admin-card .card-body {
  color: #fff;
  margin-bottom: 0;
  padding: 0.9rem;
}
.classic-admin-card .card-body p {
  font-size: 13px;
  opacity: 0.7;
  margin-bottom: 0;
}
.classic-admin-card .card-body h4 {
  margin-top: 10px;
}

.flex-container {
  align-items: center;
}
</style>


