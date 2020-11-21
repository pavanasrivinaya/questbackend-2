<template>
<nav>
     <v-app-bar app color="primary" dark>
        <v-icon 
          left 
          large
          color="white"
        >not_listed_location
        </v-icon>
        <p>
          <v-toolbar-title  class="text-uppercase white--text mt-3">

                 <a class="logo" href="https://questbackend-2.herokuapp.com/">
                Quest
            </a>
            </v-toolbar-title>
        </p>
         

          <v-spacer></v-spacer>

           <v-btn text  class="white--text mr-3" router to="/home" >Home</v-btn>
           <!-- <router-link :to="{ name: 'question-editor'}"
             class="btn btn-sm btn-danger">
            Ask Questions
           </router-link> -->
           <v-btn text  class="white--text mr-3" router to="/ask">Ask Question</v-btn>
          <v-btn  text class="white--text mr-3" href="/accounts/logout/">Logout</v-btn>
          <!-- <a href="/accounts/logout"></a> -->
    </v-app-bar>
</nav>
</template>
<style>
  a.logo {
    text-decoration: none;
    color: white;
  }
</style>