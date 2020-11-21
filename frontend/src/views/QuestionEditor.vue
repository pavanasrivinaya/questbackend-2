<template>
 <v-container>
    <h1 class="mb-3">Ask a Question</h1>
    <v-form @submit.prevent="onSubmit" ref="form" v-model="valid" lazy-validation>
      <v-textarea
        v-model="question_body"
        placeholder="What do you want to ask?"
        rows="3"
        :counter= "240"
        :rules= "textarearules"
        auto-grow
        outlined
        row-height="25"
        shaped
      ></v-textarea>
      <v-btn type="submit" :disabled="!valid"
        color="primary white--text text-center"
        class="mr-4 mb-3"
        @click="validate" rounded>Publish</v-btn> 
    </v-form>
    <div v-for="question in questions" :key="question.pk">
      <h1>{{ question.content }}</h1>

    </div>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </v-container>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "QuestionEditor",
  props: {
    slug: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      questions: [],
      question_body: null,
      error: null,
       valid: true,
      textarearules: [
        v => !!v || 'Answer is required',
        v => (v && v.length <= 240) || 'Answer must be less than 240 characters',
      ],
    }
  },
  methods: {
    onSubmit() {
      // Tell the REST API to create or update a Question Instance
      if (!this.question_body) {
        this.error = "You can't send an empty question!";
      } else if (this.question_body.length > 240) {
        this.error = "Ensure this field has no more than 240 characters!";
      } else {
        let endpoint = "/api/questions/";
        let method = "POST";
        if (this.slug !== undefined) {
          endpoint += `${ this.slug }/`;
          method = "PUT";
        }     
        apiService(endpoint, method, { content: this.question_body })
          .then(question_data => {
            this.$router.push({ 
              name: 'question', 
              params: { slug: question_data.slug }
            })          
          })  
      }
    },
    validate () {
        this.$refs.form.validate()
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
  },
   async beforeRouteEnter(to, from, next) {
    // if the component will be used to update a question, then get the question's data from the REST API
    if (to.params.slug !== undefined) {
      let endpoint = `/api/questions/${ to.params.slug }/`;
      let data = await apiService(endpoint);
      return next(vm => (vm.question_body = data.content))
    } else {
      return next();
    }   
  },
  created() {
    document.title = "Editor - QuestionTime";
  }  
}
</script>