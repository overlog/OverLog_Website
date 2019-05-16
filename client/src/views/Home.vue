<template>
  <div class="homepage">
    <login v-if="!loggedIn"></login>
    <developers v-if="!loggedIn"></developers>
    <dashboard v-if="loggedIn"></dashboard>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "homepage",
  computed: {
    ...mapState(["loggedIn"])
  }
};
</script>