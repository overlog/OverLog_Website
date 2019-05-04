<template>

  <div>
    <h1>Overlog Alarm</h1>
  <form @submit.prevent="addAllert(logtype, datetime1, datetime2, amount)">
      <select v-model="logtype" class="browser-default custom-select">
        <option value="Error">Error</option>
        <option value="Info">Info</option>
        <option value="Warning">Warning</option>
      </select>&nbsp;&nbsp;
      Start Date Time: <date-picker v-model="datetime1" lang="english" placeholder="Select Date Time" type="datetime" format="YYYY-MM-DD HH:mm:ss a" width="500"></date-picker>&nbsp;&nbsp;
      End Date Time: <date-picker v-model="datetime2" lang="english" placeholder="Select Date Time" type="datetime" format="YYYY-MM-DD HH:mm:ss a" width="500"></date-picker>&nbsp;&nbsp;
      Amount: <input type="number" placeholder="" v-model="amount" />&nbsp;&nbsp;
      <button  type="submit" class="btn btn-indigo btn-sm m-0">Add</button>&nbsp;&nbsp;
    </form>

  <hr>
    <mdb-tbl btn responsive striped>
      <mdb-tbl-head>
        <tr>

          <th>Type</th>
          <th>Start Time</th>
          <th>End Time</th>
          <th>Amount</th>
          <th></th>
        </tr>
      </mdb-tbl-head>
      <mdb-tbl-body>
          <alert-row v-for="(item, index) in rows"
          :row=item
          index=index
          v-on:itemRemoved="handleRemoveItem"
          v-bind:key="item.id"></alert-row>
      </mdb-tbl-body>
    </mdb-tbl>
  </div>
</template>

<script>
  import { mapState } from 'vuex'
  import axios from 'axios'
  import DatePicker from 'vue2-datepicker'
  import { mdbTbl, mdbTblHead, mdbTblBody } from 'mdbvue';

  export default {
    name: 'TableAdditionalPage',
    components: {
      mdbTbl,
      mdbTblHead,
      mdbTblBody,
      DatePicker,
    },
    data: function(){
      return {
        rows: [],
        datetime1: "",
        datetime2: "",
        logtype: "",
        amount: ""
      }
    },

    computed: {
      ...mapState([
        'token',
        'userID'
      ]),

    },



    methods: {
      fetchAlerts(){
        axios({ url: 'http://localhost:5000/getalert/' + this.token, params: {userID: this.userID}, method: 'GET' })
        .then((res) => {
          console.log(res)
          this.rows = res.data;
         })

      },
      handleRemoveItem(index){
        this.rows.splice(index, 1);
      },
      addAllert(logtype, datetime1, datetime2, amount){


        axios({ url: 'http://localhost:5000/addalert/' + this.token , params: {logtype: logtype, datetime1: new Date(datetime1.getTime() - datetime1.getTimezoneOffset() * 60 * 1000), datetime2: new Date(datetime2.getTime() - datetime2.getTimezoneOffset() * 60 * 1000), amount: amount, userID: this.userID}, method: 'POST' }).then(
          (res)=> {this.fetchAlerts()}
        )
      },

    },
    created() {
      this.fetchAlerts()
    }
  }
</script>


<style>
.custom-select {
	width: 150px;
}

.form-control {
	width: 10px;
}
</style>
