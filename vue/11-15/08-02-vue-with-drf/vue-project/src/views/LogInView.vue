<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="Login">
      <input type="text" v-model.trim="username">
      <input type="password" v-model.trim="password">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref(null)
const password = ref(null)
const store = useCounterStore()


const Login = function(){
  const payload = {
    username : username.value,
    password : password.value,
  }
  store.logIn(payload)
}
</script>

<style>

</style>
