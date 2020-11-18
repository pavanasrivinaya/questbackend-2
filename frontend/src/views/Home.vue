<style src="../styles/viewstyles.css"></style>

<template>
  <v-container class="home mt-2">
      <v-card class="mx-auto" max-width="1000">
        <v-card-text>
          <div v-for="question in questions" :key="question.pk">
            <p class="mb-0">
              Posted by:
              <span class="question-author">{{ question.author }}</span>
            </p>
            <h2>
              <router-link
                :to="{ name: 'question', params: { slug: question.slug } }"
                class="question-link"
              >
                {{ question.content }}
              </router-link>
            </h2>
            <p>Answers: {{ question.answers_count }}</p>
            <hr />
          </div>
          <div class="my-4">
            <p v-show="loadingQuestions">...loading...</p>
            <button
              v-show="next"
              @click="getQuestions"
              class="btn btn-sm btn-outline-success"
            >
              Load More
            </button>
          </div>
        </v-card-text>
      </v-card>
    </v-container>
</template>

<script>
import { apiService } from "../common/api.service.js";
export default {
  name: "home",
  data() {
    return {
      questions: [],
      next: null,
      loadingQuestion: false
    };
  },
  methods: {
    getQuestions() {
      let endpoint = "/api/questions/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      apiService(endpoint).then(data => {
           this.questions.push(...data.results)
           this.loadingQuestions = false;
           if(data.next) {
             this.next = data.next;
           } else {
             this.next = null;
           }
         })
    }
  },
  created() {
    this.getQuestions()
    document.title = "QuestionTime";
  }
};
</script>


