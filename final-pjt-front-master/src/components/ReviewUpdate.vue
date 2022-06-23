<template>
  <div>
    <div class="modal-header">
      <h5 class="modal-title" id="exampleModalLabel">리뷰 작성하기</h5>
      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
    </div>
    <div class="modal-body">
      <form>
        <div class="mb-3">
          <label for="recipient-name" class="col-form-label">Title:</label>
          <input type="text" class="form-control" id="recipient-name" v-model="review.title">
        </div>
        <div class="mb-3">
          <label for="recipient-name" class="col-form-label">Rank:( 0 ~ 10 )</label>
          <input type="text" class="form-control" id="recipient-name" v-model="review.rank">
        </div>
        <div class="mb-3">
          <label for="message-text" class="col-form-label">Content:</label>
          <textarea class="form-control" id="message-text" v-model="review.content"></textarea>
        </div>
      </form>
    </div>
    <div class="modal-footer">
      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
      <button @click="reviewCreate(review)" type="button" class="btn btn-primary" data-bs-dismiss="modal">작성하기</button>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewCreate',
  data: function () {
    return {
      review: {
        title: null,
        rank: null,
        content: null
      }
    }
  },
  props: {
    id: {
      type: String,
      defualt: "1",
    },
    mov: Object
  },
  methods: {

    reviewCreate: function () {
      console.log(this.$route.params.id)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.$route.params.id}/review/create/`,
        headers: {
          Authorization: `JWT ${this.$store.state.userToken}`
        },
        data: this.review,
      })
        .then(res=>{
          console.log(res)
        })
        .catch(err=>{
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>