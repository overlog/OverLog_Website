<template>
  <div class="dashboard">
    <section>
      <section class="mt-lg-5">
        <mdb-row>
          <mdb-col xl="3" md="6" class="mb-r">
            <mdb-card cascade class="cascading-admin-card">
              <div class="admin-up">
                <mdb-icon icon="money-bill-alt" far class="primary-color"/>
                <div class="data">
                  <p>SALES</p>
                  <h4>
                    <strong>$2000</strong>
                  </h4>
                </div>
              </div>
              <mdb-card-body>
                <div class="progress">
                  <div
                    aria-valuemax="100"
                    aria-valuemin="0"
                    aria-valuenow="25"
                    class="progress-bar bg-primary"
                    role="progressbar"
                    style="width: 25%"
                  ></div>
                </div>
                <mdb-card-text>Better than last week (25%)</mdb-card-text>
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
          <mdb-col xl="3" md="6" class="mb-r">
            <mdb-card cascade class="cascading-admin-card">
              <div class="admin-up">
                <mdb-icon icon="line-chart" class="warning-color"/>
                <div class="data">
                  <p>SUBSCRIPTIONS</p>
                  <h4>
                    <strong>200</strong>
                  </h4>
                </div>
              </div>
              <mdb-card-body>
                <div class="progress">
                  <div
                    aria-valuemax="100"
                    aria-valuemin="0"
                    aria-valuenow="25"
                    class="progress-bar bg grey darken-2"
                    role="progressbar"
                    style="width: 25%"
                  ></div>
                </div>
                <mdb-card-text>Worse than last week (25%)</mdb-card-text>
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
          <mdb-col xl="3" md="6" class="mb-r">
            <mdb-card cascade class="cascading-admin-card">
              <div class="admin-up">
                <mdb-icon icon="pie-chart" class="light-blue lighten-1"/>
                <div class="data">
                  <p>TRAFFIC</p>
                  <h4>
                    <strong>20000</strong>
                  </h4>
                </div>
              </div>
              <mdb-card-body>
                <div class="progress">
                  <div
                    aria-valuemax="100"
                    aria-valuemin="0"
                    aria-valuenow="75"
                    class="progress-bar grey darken-2"
                    role="progressbar"
                    style="width: 75%"
                  ></div>
                </div>
                <mdb-card-text>Worse than last week (75%)</mdb-card-text>
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
          <mdb-col xl="3" md="6" class="mb-r">
            <mdb-card cascade class="cascading-admin-card">
              <div class="admin-up">
                <mdb-icon icon="bar-chart" class="red accent-2"/>
                <div class="data">
                  <p>ORGANIC TRAFFIC</p>
                  <h4>
                    <strong>2000</strong>
                  </h4>
                </div>
              </div>
              <mdb-card-body>
                <div class="progress">
                  <div
                    aria-valuemax="100"
                    aria-valuemin="0"
                    aria-valuenow="25"
                    class="progress-bar bg-primary"
                    role="progressbar"
                    style="width: 25%"
                  ></div>
                </div>
                <mdb-card-text>Better than last week (25%)</mdb-card-text>
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
        </mdb-row>
      </section>
      <section>
        <mdb-row class="mt-5">
          <mdb-col md="9" class="mb-5">
            <mdb-card>
              <mdb-card-header>Search Log</mdb-card-header>
              <mdb-card-body>
                <div style="display: block">
                  <search-log></search-log>
                </div>
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
          <mdb-col md="3" class="mb-4">
            <mdb-card class="mb-4">
              <mdb-card-header class="text-center">Pie chart</mdb-card-header>
              <pie-chart></pie-chart>
            </mdb-card>
          </mdb-col>
        </mdb-row>
      </section>
      <section>
        <mdb-row class="mt-5">
          <mdb-col md="4" class="mb-4">
            <mdb-card class="mb-4">
              <mdb-card-header>Radar chart</mdb-card-header>
              <mdb-card-body>
                <div style="display: block">
                  <mdb-radar-chart
                    :data="radarChartData"
                    :options="radarChartOptions"
                    :height="300"
                  />
                </div>
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
          <mdb-col md="3" class="mb-4">
            <mdb-card class="mb-4">
              <mdb-card-header>Doughnut chart</mdb-card-header>
              <mdb-card-body>
                <div style="display: block">
                  <mdb-doughnut-chart
                    :data="doughnutChartData"
                    :options="doughnutChartOptions"
                    :height="300"
                  />
                </div>
              </mdb-card-body>
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
  mdbModalFooter
} from "mdbvue";
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
    mdbModalFooter
  },
  data() {
    return {
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
      showFluidModalBottom: false,
      barChartData: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
        datasets: [
          {
            label: "#1",
            data: [12, 39, 3, 50, 2, 32, 84],
            backgroundColor: "rgba(245, 74, 85, 0.5)",
            borderWidth: 1
          },
          {
            label: "#2",
            data: [56, 24, 5, 16, 45, 24, 8],
            backgroundColor: "rgba(90, 173, 246, 0.5)",
            borderWidth: 1
          },
          {
            label: "#3",
            data: [12, 25, 54, 3, 15, 44, 3],
            backgroundColor: "rgba(245, 192, 50, 0.5)",
            borderWidth: 1
          }
        ]
      },
      barChartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [
            {
              barPercentage: 1,
              gridLines: {
                display: true,
                color: "rgba(0, 0, 0, 0.1)"
              }
            }
          ],
          yAxes: [
            {
              gridLines: {
                display: true,
                color: "rgba(0, 0, 0, 0.1)"
              },
              ticks: {
                beginAtZero: true
              }
            }
          ]
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
      lineChartData: {
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
      lineChartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [
            {
              gridLines: {
                display: true,
                color: "rgba(0, 0, 0, 0.1)"
              }
            }
          ],
          yAxes: [
            {
              gridLines: {
                display: true,
                color: "rgba(0, 0, 0, 0.1)"
              }
            }
          ]
        }
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
      },
      doughnutChartData: {
        labels: ["Red", "Green", "Yellow", "Grey", "Dark Grey"],
        datasets: [
          {
            data: [300, 50, 100, 40, 120],
            backgroundColor: [
              "#F7464A",
              "#46BFBD",
              "#FDB45C",
              "#949FB1",
              "#4D5360"
            ],
            hoverBackgroundColor: [
              "#FF5A5E",
              "#5AD3D1",
              "#FFC870",
              "#A8B3C5",
              "#616774"
            ]
          }
        ]
      },
      doughnutChartOptions: {
        responsive: true,
        maintainAspectRatio: false
      }
    };
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
</style>