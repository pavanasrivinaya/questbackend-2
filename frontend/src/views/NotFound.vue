<template>
  <div class="not-found">
    <div class="container mt-3">
        <v-alert type="error">
          {{ message }}
    </v-alert>
    </div>
  </div>  
</template>

<script>
export default {
  name: "NotFound",
  data() {
    return {
      message: "404 - Page Not Found"
    }
  }
}
</script>

<style src="../styles/viewstyles.css"></style>
