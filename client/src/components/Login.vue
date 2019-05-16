<template>
  <div class="login">
    <view-wrapper v-if="!loggedIn">
      <mdb-mask class="d-flex gradient justify-content-center align-items-center">
        <mdb-container>
          <mdb-row>
            <div class="white-text text-center text-md-left col-md-6 mt-xl-5 mb-5">
              <h1 class="h1-responsive font-weight-bold">Sign up</h1>
              <hr class="hr-light">
              <h6 class="mb-4">Bazı muazzam açıklamalar.</h6>
              <mdb-btn color="white" inline="white">
                <a href="register">Sign Up!</a>
              </mdb-btn>
            </div>
            <mdb-col md="6" xl="5" class="mb-4">
              <mdb-card id="classic-card">
                <mdb-card-body class="z-depth-2 white-text">
                  <h3 class="text-center">
                    <mdb-icon icon="user"/>Login
                  </h3>
                  <hr class="hr-light">
                  <mdb-input
                    v-model="username"
                    label="Your email"
                    labelColor="white"
                    icon="envelope"
                  />
                  <mdb-input
                    v-model="password"
                    label="Your password"
                    labelColor="white"
                    icon="lock"
                    type="password"
                  />
                  <div class="text-center mt-4 black-text">
                    <mdb-btn @click="login()" color="indigo">Login</mdb-btn>
                    <div class="text-center d-flex justify-content-center white-label">
                      <a class="p-2 m-2">
                        <mdb-icon fab icon="twitter" class="white-text"/>
                      </a>
                      <a class="p-2 m-2">
                        <mdb-icon fab icon="linkedin" class="white-text"/>
                      </a>
                      <a class="p-2 m-2">
                        <mdb-icon fab icon="instagram" class="white-text"/>
                      </a>
                    </div>
                  </div>
                </mdb-card-body>
              </mdb-card>
            </mdb-col>
          </mdb-row>
        </mdb-container>
      </mdb-mask>
    </view-wrapper>
  </div>
</template>

<script>
import {
  mdbContainer,
  mdbRow,
  mdbCol,
  mdbNavbar,
  mdbNavItem,
  mdbNavbarNav,
  mdbNavbarToggler,
  ViewWrapper,
  mdbMask,
  mdbBtn,
  mdbCard,
  mdbCardBody,
  mdbInput,
  mdbIcon,
  mdbNavbarBrand
} from "mdbvue";
export default {
  name: "login",
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
    mdbNavbar,
    mdbNavItem,
    mdbNavbarNav,
    mdbNavbarToggler,
    ViewWrapper,
    mdbMask,
    mdbBtn,
    mdbCard,
    mdbCardBody,
    mdbInput,
    mdbIcon,
    mdbNavbarBrand
  },
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    login: function() {
      const username = this.username;
      const password = this.password;
      this.$store
        .dispatch("login", { username, password })
        .then(() => this.$router.push("/"));
    }
  }
};
</script>

<style>
.login .view {
  background-image: url("../assets/a.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
  height: calc(100vh + 48px);
  margin-top: -150px;
  margin-bottom: -24px;
}
.login .gradient {
  background: -webkit-linear-gradient(
    45deg,
    rgba(0, 0, 0, 0.7),
    rgba(72, 15, 144, 0.4) 15%
  );
  background: linear-gradient(
    45deg,
    rgba(0, 0, 0, 0.7),
    rgba(72, 15, 144, 0.4) 15%
  );
}
.login .card {
  background-color: rgba(126, 123, 215, 0.2);
}
.login h6 {
  line-height: 3;
}
.top-nav-collapse {
  background: #424f95 !important;
}
@media (max-width: 768px) {
  .login .navbar:not(.top-nav-collapse) {
    background: #424f95 !important;
  }
}
.login label {
  color: #fff !important;
}
</style>
