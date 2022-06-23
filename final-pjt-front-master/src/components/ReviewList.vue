<template>
  <div class="container">
    <div v-if="this.$store.getters.decodedToken" class="row">
      <ReviewListItem
        v-for="review in this.$store.state.reviews_new"
          :key="review.id"
          :review="review"
        class="col-md-4 my-2"
      />
    </div>
    <div v-else>
      
      <ReviewListItem
        v-for="review in this.$store.state.reviews"
          :key="review.id"
          :review="review"
        class="col-md-4 my-2"
      />
      <p>2</p>
    </div>
    <br>


  </div>

</template>

<script>
import ReviewListItem from '@/components/ReviewListItem'
export default {
  name: 'ReviewList',
  components: {
    ReviewListItem
  },
  created: function () {
    const movie_id = this.$route.params.id
    this.$store.dispatch('getReviews', movie_id)
    this.$store.dispatch('getReviews_new', movie_id)
  },
  
}
</script>

<style>

</style>