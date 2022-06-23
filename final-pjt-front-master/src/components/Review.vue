<template>
  <div>
    <br>
    <h2>Review</h2>
      <div v-if="this.$store.state.my_review.my_review || !this.$store.getters.decodedToken"> <!-- 이 영화에 리뷰를 작성 안했다면 -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">리뷰 작성하기</button>

        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
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
          </div>
        </div>
      </div>
      <div v-else> <!-- 이 영화에 리뷰를 작성헸다면 -->
        <div class="card" style="height:200px">
          <div class="card-body">
            <div>{{ review.id }}</div>
            <h5 class="card-title">{{this.$store.state.my_review[0].title}}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{{this.$store.state.my_review[0].rank}}</h6>
            <p class="card-text">{{this.$store.state.my_review[0].content}}</p>
            
            
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">수정</button> | 

              <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h5 class="modal-title" id="exampleModalLabel">리뷰 수정하기</h5>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                      <form>
                        <div class="mb-3">
                          <label for="recipient-name" class="col-form-label">Title:</label>
                          <input type="text" class="form-control" id="recipient-name" v-model="this.$store.state.my_review[0].title">
                        </div>
                        <div class="mb-3">
                          <label for="recipient-name" class="col-form-label">Rank:( 0 ~ 10 )</label>
                          <input type="text" class="form-control" id="recipient-name" v-model="this.$store.state.my_review[0].rank">
                        </div>
                        <div class="mb-3">
                          <label for="message-text" class="col-form-label">Content:</label>
                          <textarea class="form-control" id="message-text" v-model="this.$store.state.my_review[0].content"></textarea>
                        </div>
                      </form>
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                      <button @click="reviewUpdate" type="button" class="btn btn-primary" data-bs-dismiss="modal">작성하기</button>
                    </div>
                    
                  </div>
                </div>
              </div>
            <button class="btn btn-primary" @click="reviewDelete">삭제</button>
            
          </div>
        </div>
      </div>
      <!-- 리뷰 생성하기 버튼 모달로 구현 -->
      <!-- 리뷰 생성하기 버튼 모달로 구현 끝-->
    <div v-if="this.$store.getters.decodedToken">
      <div v-if="this.$store.getters.decodedToken.user_id === review.user">
        
        
        <ReviewList/>
      </div>
      <div v-else>

      </div>
    </div>
    <div v-else>
      <p>로그인 하셔야 리뷰를 작성할 수 있습니다.</p>
    </div>
    <ReviewList/>



    
  </div>
</template>

<script>
import axios from 'axios'

import ReviewList from '@/components/ReviewList.vue'

export default {
  name: 'ReviewCreate',
  components: {
    ReviewList,

  },
  data: function () {
    return {
      review: {
        title: null,
        rank: null,
        content: null,
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

    reviewCreate: function (review) {
      console.log(this.$store.getters.decodedToken)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.$route.params.id}/review/create/`,
        headers: {
          Authorization: `JWT ${this.$store.state.userToken}`
        },
        data: review,
      })
        .then(res=>{
          console.log(res.data)
          this.$store.dispatch('createReview', res.data)
        })
        .catch(err=>{
          console.log(err)
        })
    },
    reviewDelete: function () {
      const review_id = this.review.id
      this.$store.dispatch('reviewDelete', review_id)
    },
    reviewUpdate: function () {
    }

  },

  created: function () {
    const movie_id = this.$route.params.id
    this.$store.dispatch('myReviewInMovie', movie_id)
  }
}
</script>

<style>

</style>