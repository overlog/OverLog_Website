<template>
  <div class="register2">
    <view-wrapper>
      <mdb-mask class="d-flex gradient justify-content-center align-items-center">
        <mdb-container>
          <mdb-row>
            <div class="white-text text-center text-md-left col-md-6 mt-xl-5 mb-5"></div>
            <mdb-col md="6" xl="5" class="mb-4">
              <mdb-card id="classic-card">
                <mdb-card-body class="z-depth-2 white-text">
                  <h3 class="text-center">
                    <mdb-icon icon="user"/>Register:
                  </h3>
                  <hr class="hr-light">
                  <mdb-input label="Your name" labelColor="white" icon="user"/>
                  <mdb-input label="Your email" labelColor="white" icon="envelope"/>
                  <mdb-input label="Your password" labelColor="white" icon="lock" type="password"/>
                  <div class="text-center mt-4 black-text">
                    <mdb-btn color="indigo">Sign Up</mdb-btn>
                    <hr class="hr-light">
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
    <mdb-container>
      <mdb-row class="py-5">
        <mdb-col md="12" class="text-center">
          <p>I only trust two people in this world, First is me, and second is not you.</p>
        </mdb-col>
      </mdb-row>
    </mdb-container>
  </div>
</template>

<script>
import { mapState } from "vuex";
//import { mapActions} from 'vuex'
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
  name: "Register",
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
      email: "",
      password: "",
      companyName: ""
    };
  },
  computed: {
    ...mapState(["registeredSuccessfully", "registerError"])
  }
};
</script>

<style>
.register2 .view {
  background-image: url("../assets/a.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
  height: calc(100vh + 48px);
  margin-top: -150px;
}

.register2 .gradient {
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

.register2 .card {
  background-color: rgba(126, 123, 215, 0.2);
}

.register2 h6 {
  line-height: 3;
}

.top-nav-collapse {
  background: #424f95 !important;
}

@media (max-width: 768px) {
  .register2 .navbar:not(.top-nav-collapse) {
    background: #424f95 !important;
  }
}

.register2 label {
  color: #fff !important;
}
</style>