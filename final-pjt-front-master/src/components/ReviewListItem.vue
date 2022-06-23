<template>
  <div>
    <div class="card" style="height:200px">
      <div class="card-body">
        <div>{{ review.id }}</div>
        <h5 class="card-title">{{ review.title }}</h5>
        <h6 class="card-subtitle mb-2 text-muted">{{ review.rank }}</h6>
        <p class="card-text">{{ review.content }}</p>
        
      </div>
    </div>

  </div>
</template>

<script>

// import axios from 'axios'
export default {
  name: 'ReviewListItem',
  
  props: {
    review: Object
  },
  
  methods: {
    reviewDelete: function () {
      const review_id = this.review.id
      this.$store.dispatch('reviewDelete', review_id)
    },
    reviewUpdate: function () {

    }
  }
  
}
</script>

<style>

</style>