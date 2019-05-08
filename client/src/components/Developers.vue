<template>
  <div class="developers">
    <view-wrapper>
      <mdb-mask class="d-flex gradient justify-content-center align-items-center">
        <mdb-container>
          <mdb-row>
            <mdb-col sm="3">
              <mdb-card testimonial>
                <mdb-card-up color="indigo" class="lighten-1"></mdb-card-up>
                <mdb-card-avatar color="white" class="mx-auto">
                  <img src="@/assets/developers/ali.png" class="rounded-circle">
                </mdb-card-avatar>
                <mdb-card-body>
                  <mdb-card-title>Ali Gediz</mdb-card-title>
                  <hr>
                  <p>
                    <mdb-icon icon="quote-left"/>yolumuz yol değil ama manzarası güzel.
                  </p>
                </mdb-card-body>
              </mdb-card>
            </mdb-col>
            <mdb-col sm="3">
              <mdb-card testimonial>
                <mdb-card-up gradient="aqua" class="lighten-1"></mdb-card-up>
                <mdb-card-avatar color="white" class="mx-auto">
                  <img src="@/assets/developers/muhammet.jpg" class="rounded-circle">
                </mdb-card-avatar>
                <mdb-card-body>
                  <mdb-card-title>Muhammet Ali Inal</mdb-card-title>
                  <hr>
                  <p>
                    <mdb-icon icon="quote-left"/>özendiğiniz hayatı yaşamakla meşkulüm.
                  </p>
                </mdb-card-body>
              </mdb-card>
            </mdb-col>
            <mdb-col sm="3">
              <mdb-card testimonial>
                <mdb-card-up color="indigo" class="lighten-1"></mdb-card-up>
                <mdb-card-avatar color="white" class="mx-auto">
                  <img src="@/assets/developers/osman.jpg" class="rounded-circle">
                </mdb-card-avatar>
                <mdb-card-body>
                  <mdb-card-title>Osman Unal</mdb-card-title>
                  <hr>
                  <p>
                    <mdb-icon icon="quote-left"/>gönlünde yer yoksa güzelim, ben ayakta da giderim.
                  </p>
                </mdb-card-body>
              </mdb-card>
            </mdb-col>
            <mdb-col sm="3">
              <mdb-card testimonial>
                <mdb-card-up gradient="aqua" class="lighten-1"></mdb-card-up>
                <mdb-card-avatar color="white" class="mx-auto">
                  <img src="@/assets/developers/yunus.jpg" class="rounded-circle">
                </mdb-card-avatar>
                <mdb-card-body>
                  <mdb-card-title>Yunus Atahan</mdb-card-title>
                  <hr>
                  <p>
                    <mdb-icon icon="quote-left"/>doktor değilim ama hastam çok.
                  </p>
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
  name: "ClassicFormPage",
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
  }
};
</script>

<style>
.developers .view {
  background-image: url("../assets/background.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
  height: calc(100vh + 48px);
  margin-top: -150px;
}

.developers .gradient {
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

.developers .card {
  background-color: rgba(126, 123, 215, 0.2);
}

.developers h6 {
  line-height: 3;
}

.top-nav-collapse {
  background: #424f95 !important;
}

@media (max-width: 768px) {
  .developers .navbar:not(.top-nav-collapse) {
    background: #424f95 !important;
  }
}

.developers label {
  color: #fff !important;
}
</style>