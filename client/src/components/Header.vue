<template>
  <div>
    <mdb-navbar dark color="black" position="top">
      <mdb-navbar-brand href="#" target="_blank">OVERLOG</mdb-navbar-brand>
      <mdb-navbar-toggler>
        <mdb-navbar-nav left>
          <mdb-nav-item to="/" waves-fixed>Home</mdb-nav-item>
        </mdb-navbar-nav>
        <mdb-navbar-nav right>
          <button
            v-on:click="logout"
            v-if="loggedIn"
            class="btn btn-outline-white btn-md my-2 my-sm-0 ml-3"
            href="/"
            waves-fixed
          >Logout</button>
          <!-- <span v-if="loggedIn"> | <a @click="logout">Logout</a></span>  -->
        </mdb-navbar-nav>
      </mdb-navbar-toggler>
    </mdb-navbar>
  </div>
</template>

<script>
import { mapState } from "vuex";
import {
  mdbNavbar,
  mdbNavbarBrand,
  mdbNavItem,
  mdbNavbarNav,
  mdbNavbarToggler,
  mdbFormInline,
  mdbInput
} from "mdbvue";

export default {
  name: "Header",
  components: {
    mdbNavbar,
    mdbNavbarBrand,
    mdbNavItem,
    mdbNavbarNav,
    mdbNavbarToggler,
    mdbFormInline,
    mdbInput
  },
  computed: {
    ...mapState(["loggedIn"])
  },
  methods: {
    logout: function() {
      this.$store.dispatch("logout").then(() => this.$router.push("/"));
    }
  }
};
</script>

<style>
</style>


/*

*/
