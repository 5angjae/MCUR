<template>
  <div>
    <br>
    <div class="container">
      <br>
      <h1>Login</h1>
      <div class="mb-3 row">
        <label for="text" class="col-sm-2 col-form-label">사용자 이름</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="staticEmail" v-model="credential.username">
        </div>
      </div>
      <div class="mb-3 row">
        <label for="inputPassword" class="col-sm-2 col-form-label">비밀번호</label>
        <div class="col-sm-10">
          <input type="password" class="form-control" id="inputPassword" v-model="credential.password">
        </div>
      </div>
      <button class="btn btn-primary mb-3" @click="getJWT">로그인</button>
    </div>
   
  </div>
</template>

<script>
export default {
  name: 'Login',
  data: function () {
    return {
      credential: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    getJWT: function () {
      this.$store.dispatch('getJWT', this.credential)
      // if (this.$store.getters.decodedToken) {
      //   }
      this.$router.push({name: 'Home'})
    }
  },
  created: function () {
    if (this.$store.getters.decodedToken) {
      this.$router.push({name: 'Home'})
    }
  }
}
</script>

<style>

</style>