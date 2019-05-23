<template>
  <div class="developers">
    <mdb-container>
      <mdb-row class="py-5">
        <mdb-col md="12" class="text-center">
          <p class="font-weight-bold">DO MORE WITH YOUR LOG DATA</p>
        </mdb-col>
      </mdb-row>
    </mdb-container>
    <mdb-container>
      <mdb-row>
        <mdb-col sm="3">
          <mdb-card testimonial>
            <mdb-card-up color="indigo" class="lighten-1"></mdb-card-up>
            <mdb-card-avatar color="white" class="mx-auto">
              <img src="@/assets/developers/ali.png" class="rounded-circle">
            </mdb-card-avatar>
            <mdb-card-body>
              <mdb-card-title class="font-weight-bold">Ali Gediz</mdb-card-title>
              <hr>
              <p>
                <mdb-icon/>Student - Backend Developer
              </p>
              <a class="fb-ic ml-0" href="https://github.com/aligedizx">
                <i class="fab fa-github black-text mr-lg-4"></i>
              </a>
              <a class="tw-ic" href="https://twitter.com/AliGedizX">
                <i class="fab fa-twitter black-text mr-lg-4"></i>
              </a>
              <a class="li-ic" href="https://www.linkedin.com/in/aligedizx/">
                <i class="fab fa-linkedin-in black-text mr-lg-4"></i>
              </a>
              <a class="ins-ic" href="https://www.instagram.com/aligedizx/">
                <i class="fab fa-instagram black-text mr-lg-4"></i>
              </a>
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
              <mdb-card-title class="font-weight-bold">Muhammet Ali Inal</mdb-card-title>
              <hr>
              <p>
                <mdb-icon/>Student - Frontend Developer
              </p>
              <a class="li-ic" href="https://github.com/muhammetaliinal">
                <i class="fab fa-github black-text mr-lg-4"></i>
              </a>
              <a class="tw-ic" href="https://twitter.com/muhammetaliinal">
                <i class="fab fa-twitter black-text mr-lg-4"></i>
              </a>
              <a class="fb-ic ml-0" href="https://www.facebook.com/profile.php?id=1421983528">
                <i class="fab fa-facebook black-text mr-lg-4"></i>
              </a>
              <a class="ins-ic" href="https://www.instagram.com/muhammet.inal/">
                <i class="fab fa-instagram black-text mr-lg-4"></i>
              </a>
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
              <mdb-card-title class="font-weight-bold">Osman Unal</mdb-card-title>
              <hr>
              <p>
                <mdb-icon/>Student - Frontend Developer
              </p>
              <a class="fb-ic ml-0" href="https://github.com/osmnnl">
                <i class="fab fa-github black-text mr-lg-4"></i>
              </a>
              <a class="tw-ic" href="https://twitter.com/osman_unal">
                <i class="fab fa-twitter black-text mr-lg-4"></i>
              </a>
              <a class="li-ic" href="https://www.linkedin.com/in/osmnnl/">
                <i class="fab fa-linkedin-in black-text mr-lg-4"></i>
              </a>
              <a class="ins-ic" href="https://www.instagram.com/osmn.nl/">
                <i class="fab fa-instagram black-text mr-lg-4"></i>
              </a>
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
              <mdb-card-title class="font-weight-bold">Yunus Atahan</mdb-card-title>
              <hr>
              <p>
                <mdb-icon/>Student - Backend Developer
              </p>
              <a class="fb-ic ml-0" href="https://github.com/y961996">
                <i class="fab fa-github black-text mr-lg-4"></i>
              </a>
              <a class="li-ic" href="https://www.linkedin.com/in/yunus-atahan-a037a6144/">
                <i class="fab fa-linkedin-in black-text mr-lg-4"></i>
              </a>
              <a class="ins-ic" href="https://www.instagram.com/yunusatahan/">
                <i class="fab fa-instagram black-text mr-lg-4"></i>
              </a>
            </mdb-card-body>
          </mdb-card>
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
  name: "developers",
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

