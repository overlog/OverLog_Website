<template>
  <div class="example">
    <apexchart width="500" type="line" :options="chartOptions" :series="series"></apexchart>
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
            horizontal: true
          }
        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
        }
      },
      series: [{
        name: 'series-1',
        data: [30, 40, 45, 50, 49, 60, 70, 91]
      }]
    }
  },
  methods: {
    fetchlogs() {
      console.log("...")
        fetch('http://127.0.0.1:5000/logs')
        .then((res) => {return res.json() })
        .then( (res) => { this.setTypes(res) } )
    },
    setTypes(res){
      var dates = [];
      var types = [];
      var len = Object.keys(res).length;
      var num = 0;
      for(let i = 2; i < len; i++){
        var date = res[i]['date'].split(" ")[0];
        if(dates.indexOf(date) == -1){
          dates.push(date);
          types.push(num);
          num = 0;
        }else{
          num++;
        }
      }

      this.series =         this.series = [{
                data: types
              }];
      this.xaxis = this.xaxis = [{
                categories: dates
      }];
      console.log(types);
      console.log(dates)
    },

      updateChart() {
        this.fetchlogs()
      
        const colors = ['#008FFB', '#00E396', '#FEB019', '#FF4560', '#775DD0']

        // Make sure to update the whole options config and not just a single property to allow the Vue watch catch the change.
        this.chartOptions = {
          colors: [colors[Math.floor(Math.random()*colors.length)]]
        };
      }
    }
}
</script>