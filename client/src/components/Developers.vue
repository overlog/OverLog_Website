<template>
  <div class="developers">
    <mdb-container>
      <mdb-row class="py-5">
        <mdb-col md="12" class="text-center">
          <p>I only trust two people in this world, First is me, and second is not you.</p>
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

