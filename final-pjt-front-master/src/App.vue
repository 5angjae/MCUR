<template>
  <div id="app">
    <nav id="navbar-example2" class="navbar navbar-light bg-light px-3 sticky-top">
      <router-link class="nav-link" to="/">Recommend MCU</router-link>
      <ul class="nav nav-pills me-5" v-if="this.$store.getters.decodedToken">
        <span class="nav-item">
          <router-link class="nav-link" to="/">Home</router-link>
        </span>
        <span class="nav-item">
          <router-link class="nav-link" to="/recommend">Recommend</router-link>
        </span>
        <span class="nav-item">
          <router-link class="nav-link" @click.native="deleteJWT" to="#">Logout</router-link>
        </span>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">영화 목록</a>
          <ul class="dropdown-menu">
            
            <li><a class="dropdown-item" v-for="movie in $store.state.movie_list"
              :key="movie.id"
              :movie="movie"
              :href="'#'+movie.title">{{ movie.title }}</a></li>
          </ul>
        </li>
      </ul>
      <ul class="nav nav-pills me-5" v-else>
        <span class="nav-item">
          <router-link class="nav-link" to="/">Home</router-link>
        </span>
        <span class="nav-item">
          <router-link class="nav-link" :to="{ name: 'Signup' }">Signup</router-link>
        </span>
        <span class="nav-item">
          <router-link class="nav-link" :to="{ name: 'Login' }">Login</router-link>
        </span>
      
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">영화 목록</a>
          <ul class="dropdown-menu">
            
            <li><a class="dropdown-item" v-for="movie in $store.state.movie_list"
              :key="movie.id"
              :movie="movie"
              :href="'#'+movie.title">{{ movie.title }}</a></li>
            
          </ul>
        </li>
      </ul>
    </nav>
    
    <router-view @login="isLogin = true"/>
  </div>
</template>

<script>
import axios from 'axios'

const MOVIE_URL = 'http://127.0.0.1:8000/movies/index/'
// 수정 필요

export default {
  name: 'App',
  methods: {
    deleteJWT: function () {
      this.$store.dispatch('deleteJWT')
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    if (!this.$store.getters.decodedToken) {
      this.$router.push({name: 'Login'})
    }
    axios({
      method: 'get',
      url: MOVIE_URL
    })
      .then((res)=>{
        this.$store.dispatch('getMovies', res.data)
      })
      .catch((error)=>{
        console.log(error)
      })
    
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  }


}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 20px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.dropdown-menu {         
  max-height: 200px;
  overflow-y: auto;
}
</style>
