<template>
  <div class="recommend">
    <RecommendList/>
  </div>
</template>

<script>
// @ is an alias to /src
import RecommendList from '@/components/RecommendList.vue'
import axios from 'axios'

export default {
  name: 'Recommend',
  components: {
    RecommendList
  },
  created: function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/rlr/',
      headers: {
        Authorization: `JWT ${this.$store.state.userToken}`
      }
    })
      .then(res=>{
        
        this.$store.dispatch('getRecommend', res.data)
      })
      .catch(err=>{
        console.log(err)
      })
    
  }
}
</script>
