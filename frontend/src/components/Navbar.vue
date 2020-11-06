<template>
<nav>
     <v-app-bar app color="primary" dark>
        <v-icon 
          left 
          large
          color="white"
        >not_listed_location
        </v-icon>
          <v-toolbar-title class="text-uppercase white--text">
               <span class="font-weight-light">Quest</span>
          </v-toolbar-title>

          <v-spacer></v-spacer>

           <v-btn text  class="white--text mr-3" router to="/home" >Home</v-btn>
           <v-btn text  class="white--text mr-3" router to="/ask">Ask Question</v-btn>
          <v-btn  text class="white--text mr-3" href="/accounts/logout/">Logout</v-btn>
          <!-- <a href="/accounts/logout"></a> -->
    </v-app-bar>
</nav>
</template>