<template>
  <tr>
    <td>{{ row.type }}</td>
    <td>{{ row.starttime }}</td>
    <td>{{ row.endtime }}</td>
    <td>{{ row.amount }}</td>
    <td>
        <button @click="cancel(row.id, index)" type="button" class="btn btn-indigo btn-sm m-0">Cancel</button>
    </td>
  </tr>
</template>

<script>
  import { mapState } from 'vuex'
  import axios from 'axios'
  export default{
    props: ['row', 'index'],


    computed: {
      ...mapState([
        'token'
        
      ]),

    },

    methods: {
      cancel: function(id, index){
        console.log(id)
        axios({ url: 'http://localhost:5000/deletealert/' + this.token, params: {id: id}, method: 'POST' })
        this.$emit('itemRemoved', index);
      }

    }
}

</script>
