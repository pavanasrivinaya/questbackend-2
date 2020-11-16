<template>
  <div class="container mt-2">
    <h1 class="mb-3">Edit Your Answer</h1>
    <v-form @submit.prevent="onSubmit" ref="form"
    v-model="valid"
    lazy-validation>
      <v-textarea 
        v-model="answerBody" 
        class="form-control" 
        rows="3"
        :counter="300"
        :rules= "textarearules"
        required
      ></v-textarea>
      <br>
      <v-btn
        type="submit" 
        class="success"
        >Publish yours-- answer
      </v-btn>
    <v-form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "AnswerEditor",
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      questionSlug: null,
      answerBody: null,
      error: null,
      valid: true,
      textarearules: [
        v => !!v || 'Answer is required',
        v => (v && v.length <= 300) || 'Answer must be less than 300 characters',
      ],
    }
  },
  methods: {
    onSubmit() {
      if (this.answerBody) {
        let endpoint = `/api/answers/${this.id}/`;
        apiService(endpoint, "PUT", { body: this.answerBody })
          .then(() => {
            this.$router.push({
              name: "question",
              params: { slug: this.questionSlug }
            })
          })
      } else {
        this.error = "You can't submit an empty answer!";
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // get the answer's data from the REST API and set two data properties for the component
    let endpoint = `/api/answers/${to.params.id}/`;
    let data = await apiService(endpoint);
    return next(vm => (
      vm.answerBody = data.body,
      vm.questionSlug = data.question_slug
    ));
  }
};
</script>