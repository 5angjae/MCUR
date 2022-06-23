import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import jwt_decode from 'jwt-decode'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    movie_list: [],
    movie_detail: null,
    recommend_list: [],
    recommend_hero: null,
    userToken: null,
    reviews: null,
    reviews_new: null,
    my_review: null,
  },
  mutations: {
    GET_MOVIES: function (state, movies) {
      state.movie_list = movies
    },
    GET_MOVIE_DETAIL: function (state, movie) {
      console.log(movie)
      state.movie_detail = movie
    },
    RECOMMEND_MOVIES: function (state, movies) {
      
      state.recommend_list = movies
      state.recommend_hero = state.recommend_list[0]
      state.recommend_list.splice(0, 1)
      
    },
    saveJWT: function (state, token) {
      state.userToken = token
    },
    deleteJWT: function (state) {
      state.userToken = null
    },
    getReviews: function (state, data) {
      state.reviews = data
    },
    getReviews_new: function (state, data) {
      state.reviews_new = data
    },
    createReview: function (state, review) {
      state.reviews.push(review)
    },
    reviewDelete: function (state, data) {
      var index = state.reviews.findIndex(review => review.id === data.id)
      state.reviews.splice(index, 1)
    },
    MY_REVIEW: function (state, data) {
      state.my_review = data
    }
  },
  actions: {
    getMovies: function ({ commit }, movies) {
      commit('GET_MOVIES', movies)
    },
    getMovieDetail: function ({commit}, movie_id) {
      
      axios ({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movie_id}/`
      })
        .then((res)=>{
          
          commit('GET_MOVIE_DETAIL', res.data)
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    myReviewInMovie: function (context, movie_id) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movie_id}/my_review/`,
        headers: {
          Authorization: `JWT ${context.state.userToken}`
        }
      })
        .then((res)=>{
          console.log(res.data)
          context.commit('MY_REVIEW', res.data)
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    getRecommend: function ({ commit }, movies) {
      
      commit('RECOMMEND_MOVIES', movies)
      
    },
    getJWT: function (context, credentials) {
      // console.log(context, credentials)
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/api-token-auth/`,
        data: credentials,
      })
        .then((res)=>{
          console.log(res.data.token)
          context.commit('saveJWT', res.data.token)
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    deleteJWT: function (context) {
      context.commit('deleteJWT')
    },
    getReviews: function (context, movie_id) {
      console.log(context)
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/${movie_id}/reviews/`,
        headers: {
          Authorization: `JWT ${context.state.userToken}`
        }
      })
        .then(res=>{
          context.commit('getReviews', res.data)
        })
        .catch(err=>{
          console.log(err)
        })
    },
    getReviews_new: function (context, movie_id) {
      console.log(context)
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/${movie_id}/reviews2/`,
        headers: {
          Authorization: `JWT ${context.state.userToken}`
        }
      })
        .then(res=>{
          console.log(res.data)
          context.commit('getReviews_new', res.data)
        })
        .catch(err=>{
          console.log(err)
        })
    },
    createReview: function (context, review) {
      context.commit('createReview', review)
    },
    reviewDelete: function (context, review_id) {
      axios({
        
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/review/${review_id}/`,
        headers: {
          Authorization: `JWT ${context.state.userToken}`
        }
      })
        .then(res=>{
          context.commit('reviewDelete', res.data)
        })
        .then(err=>{
          console.log(err)
        })
      
    },
    

  },
  modules: {
  },
  getters: {
    decodedToken: function (state) {
      if (state.userToken) {
        return jwt_decode(state.userToken)
      }
      else {
        return null
      }
    }
  }
})
