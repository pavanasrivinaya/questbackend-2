<template>
  <v-app>
   <Navbar />
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import { apiService } from "@/common/api.service.js"
import Navbar from "@/components/Navbar.vue";

export default {
  name: "App",

  components: {
    Navbar
  },
  methods: {
    async setUserInfo() {
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      window.localStorage.setItem("username", requestUser);
    }
  },
  created() {
    this.setUserInfo()
  }
};
</script>

<style>
html, body {
  height: 100%;
  font-family: "Playfair Display", serif;
}

.btn:focus {
  box-shadow: none !important;
}
</style>