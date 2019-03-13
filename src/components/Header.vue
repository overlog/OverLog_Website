<template>
  <mdb-navbar class="flexible-navbar white" light position="top" scrolling>
      <mdb-navbar-brand href="#" target="_blank">OVERLOG</mdb-navbar-brand>
      <mdb-navbar-toggler>
        <mdb-navbar-nav left>
          <mdb-nav-item to="/" waves-fixed active class="active">Home</mdb-nav-item>
          <mdb-nav-item href="/about" waves-fixed>About OVERLOG</mdb-nav-item>
        </mdb-navbar-nav>
      </mdb-navbar-toggler>
    </mdb-navbar>
</template>

<script>
import { mdbContainer, mdbNavbar, mdbNavbarBrand, mdbNavItem, mdbNavbarNav, mdbNavbarToggler, mdbBtn, mdbIcon, mdbListGroup, mdbListGroupItem, mdbCardBody, mdbFooter, waves } from 'mdbvue'

export default {
  name: 'Header',
  components: {
    mdbContainer,
    mdbNavbar,
    mdbNavbarBrand,
    mdbNavItem,
    mdbNavbarNav,
    mdbNavbarToggler,
    mdbBtn,
    mdbListGroup,
    mdbListGroupItem,
    mdbIcon,
    mdbCardBody,
    'ftr': mdbFooter,
  }
}
</script>

<style>

</style>