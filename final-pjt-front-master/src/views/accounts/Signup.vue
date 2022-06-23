<template>
  <div>
    <br>
    <div class="container">
      <br>
      <h1>Signup</h1>
      <div class="mb-3 row">
        <label for="username" class="col-sm-2 col-form-label">사용자 이름</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="username" v-model="credentials.username">
        </div>
      </div>
      <div class="mb-3 row">
        <label for="password" class="col-sm-2 col-form-label">비밀번호</label>
        <div class="col-sm-10">
          <input type="password" class="form-control" id="password" v-model="credentials.password">
        </div>
      </div>
      <div class="mb-3 row">
        <label for="passwordConfirmation" class="col-sm-2 col-form-label">비밀번호 확인</label>
        <div class="col-sm-10">
          <input type="password" class="form-control" id="passwordConfirmation"  v-model="credentials.passwordConfirmation">
        </div>

      </div>
      <button class="btn btn-primary mb-3" @click="signup(credentials)">회원가입</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'Login' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
