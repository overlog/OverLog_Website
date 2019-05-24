<template>
  <mdb-col xl="3" md="6" class="mb-r">
    <mdb-card cascade class="cascading-admin-card">
      <div class="admin-up">
        <mdb-icon icon="money-bill-alt" far class="primary-color"/>
        <div class="data">
          <p>{{ type }}</p>
          <h4>
            <strong>
              <span>{{ count }}</span>
            </strong>
          </h4>
        </div>
      </div>
      <mdb-card-body>
        <div class="progress">
          <div

            class="progress-bar bg-primary"
            role="progressbar"
            :style=width
          ></div>
        </div>
        <mdb-card-text v-if="rate > 0"> More than last week {{ Math.abs(rate) }}</mdb-card-text>
        <mdb-card-text v-if="rate < 0"> Less than last week {{ Math.abs(rate) }}</mdb-card-text>
      </mdb-card-body>
    </mdb-card>
  </mdb-col>
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
import { filter } from 'minimatch';

export default {
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
  props: ["res"],

  computed: {
    type: function() {
      return this.res[0]["type"];
    },
    count: function() {
      return Object.keys(this.res).length;
    },
    rate: function() {
      return this.calculateRate(this.res);
    },
    width: function(){
        return "width:" + Math.abs(this.rate) + "%"
    }
  },

  methods: {
      abs(sayi){},


    calculateRate(res) {
      var endDate = new Date();
      endDate = new Date(
        endDate.getTime() - endDate.getTimezoneOffset() * 60 * 1000
      );

      var substraction = 60 * 60 * 24 * 1000;

      var midDate = new Date(endDate - substraction);
      var startDate = new Date(midDate - substraction);

      var first = 0;
      var second = 0;

      res.map(log => {
        if (
          new Date(log["date"]).getTime() > startDate.getTime() &&
          new Date(log["date"]).getTime() < midDate.getTime()
        ) {
          first++;
        } else if (
          new Date(log["date"]).getTime() > midDate.getTime() &&
          new Date(log["date"]).getTime() < endDate.getTime()
        ) {
            second++
        }
      });
      
      return (second - first) / first * 100 
    }
  }
};
</script>

<style scoped>
.cascading-admin-card {
  margin: 20px 0;
}
.cascading-admin-card .admin-up {
  margin-left: -60%;
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



