<template>
  <div class="example">
    <apexchart width="500" type="bar" :options="chartOptions" :series="series"></apexchart>
     <div>
       <button @click="updateChart">Update!</button>
    </div>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
  name: 'BarExample',
  components:{
    apexchart: VueApexCharts,
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
      series: [{
        name: 'series-1',
        data: [30, 40, 45]
      }]
    }
  },
  methods: {

    fetchlogs() {
      console.log("...")
        fetch('http://127.0.0.1:5000/')
        .then((res) => {return res.json() })
        .then( (res) => { this.setnums(res) } )
    },

    setnums(res){
      var e = 0
      var i = 0
      var w = 0
      var len = Object.keys(res).length

      for (var j = 0; j < len; j++) {
        if(res[j+1]['type'] == 'i'){
          i++

        }
        else if(res[j+1]['type'] == 'e'){
          e++

        }
        else if(res[j+1]['type'] == 'w'){
          w++
        }
      }
      this.series =         this.series = [{
                data: [e,w,i]
              }]

    },


      updateChart() {
        this.fetchlogs()
        //const colors = ['#008FFB', '#00E396', '#FEB019', '#FF4560', '#775DD0']

        // Make sure to update the whole options config and not just a single property to allow the Vue watch catch the change.
        this.chartOptions = {
          colors: ['#FEB019', '#FF4560', '#775DD0'],


        };
        // In the same way, update the series option
      }
    }
}
</script>
