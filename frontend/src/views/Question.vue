<style src="../styles/viewstyles.css"></style>

<template>
  <v-container class="mt-2">
    <v-container v-if="question" >
      <h1>{{ question.content }}</h1>
      <QuestionActions
        v-if="isQuestionAuthor"
        :slug="question.slug"
      />
      <p class="mb-0">Posted by:
        <span class="author-name">{{ question.author }}</span>                                  
      </p>
      <p>{{ question.created_at }}</p>
      <hr>
      <div v-if="userHasAnswered">
        <v-alert  dense
      text
      type="success">
You've written an answer!  
  </v-alert>
        <!-- <p class="answer-added">You've written an answer!</p> -->
      </div>
      <v-container v-else-if="showForm">
         <v-col>
            Answer the Question
          </v-col>
        <v-form  @submit.prevent="onSubmit" ref="form" v-model="valid" lazy-validation>
         
            <v-textarea 
              v-model="newAnswerBody"
              placeholder="Share Your Knowledge!"
              :counter= "240"
              :rules= "textarearules"
              auto-grow
              outlined
              shaped
            ></v-textarea>
            <v-btn type="submit" :disabled="!valid" color="primary white--text text  btr"
               @click="validate" rounded>Submit Your Answer.</v-btn>
        </v-form>
          <v-alert v-if="error" type="error" class="mt-2">{{ error }}</v-alert>
        <!-- <p v-if="error" class="error mt-2">{{ error }}</p> -->
      </v-container>
      <div v-else>
        <v-btn
          color="white--text text-center primary"
          @click="showForm = true"
          btr
          rounded>Answer the Question
        </v-btn>
      </div>
      <hr>
    </v-container>
    <div v-else>
        <v-alert type="error">
          Question already exists.Ask another question
        <a href="https://questbackend-2.herokuapp.com/ask" rel="noopener" class="text-center">Ask a new question</a>
    </v-alert>

    </div>
    <div v-if="question" class="container">
      <AnswerComponent 
        v-for="answer in answers"
        :answer="answer"
        :requestUser="requestUser"
        :key="answer.id"
        @delete-answer="deleteAnswer"
      />
      <div class="my-4">
        <p v-show="loadingAnswers">...loading...</p>
        <button
          v-show="next"
          @click="getQuestionAnswers"
          class="btn btn-sm btn-outline-success"
          >Load More
        </button>
      </div>
    </div>
  </v-container>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import AnswerComponent from "@/components/Answer.vue";
import QuestionActions from "@/components/QuestionActions.vue";
export default {
  name: "Question",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    AnswerComponent,
    QuestionActions
  },
  data() {
    return {
      question: {},
      answers: [],
      next: null,
      loadingAnswers: false,
      newAnswerBody: null,
      error: null,
      userHasAnswered: false,
      showForm: false,
      requestUser: null,
      valid: true,
      textarearules: [
        v => !!v || 'Answer is required',
        v => (v && v.length <= 240) || 'Answer must be less than 240 characters',
      ],
    }
  },
  computed: {
    isQuestionAuthor() {
      // return true if the logged in user is also the author of the question instance
      return this.question.author === this.requestUser;
    }
  },
  methods: {
    validate () {
        this.$refs.form.validate()
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
    setPageTitle(title) {
      // set a given title string as the webpage title
      document.title = title;
    },
    setRequestUser() {
      // the username has been set to localStorage by the App.vue component
      this.requestUser = window.localStorage.getItem("username");
    },
    getQuestionData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/questions/${this.slug}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.question = data;
            this.userHasAnswered = data.user_has_answered;
            this.setPageTitle(data.content)
          } else {
            this.question = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    },
    getQuestionAnswers() {
      // get a page of answers for a single question from the REST API's paginated 'Questions Endpoint'
      let endpoint = `/api/questions/${this.slug}/answers/`;
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingAnswers = true;
      apiService(endpoint)
        .then(data => {
          this.answers.push(...data.results);
          this.loadingAnswers = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        })
    },
    onSubmit() {
      // Tell the REST API to create a new answer for this question based on the user input, then update some data properties
      if (this.newAnswerBody) {
        let endpoint = `/api/questions/${this.slug}/answer/`;
        apiService(endpoint, "POST", { body: this.newAnswerBody })
          .then(data => {
            this.answers.unshift(data)
          })
        this.newAnswerBody = null;
        this.showForm = false;
        this.userHasAnswered = true;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "You can't send an empty answer!";
      }
    },
    async deleteAnswer(answer) {
      // delete a given answer from the answers array and make a delete request to the REST API
      let endpoint = `/api/answers/${answer.id}/`;
      try {
        await apiService(endpoint, "DELETE")
        this.$delete(this.answers, this.answers.indexOf(answer))
        this.userHasAnswered = false;
      }
      catch (err) {
        console.log(err)
      }
    }
  },
  created() {
    this.getQuestionData()
    this.getQuestionAnswers()
    this.setRequestUser()
  }
}
</script>

