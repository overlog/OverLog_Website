<template>
  <mdb-navbar class="flexible-navbar white" light position="top" scrolling>
      <mdb-navbar-brand href="#" target="_blank">OVERLOG</mdb-navbar-brand>
      <mdb-navbar-toggler>
        <mdb-navbar-nav left>
          <mdb-nav-item to="/" waves-fixed>Home</mdb-nav-item>
          <mdb-nav-item href="/about" waves-fixed>About</mdb-nav-item>
        </mdb-navbar-nav>
      </mdb-navbar-toggler>
    </mdb-navbar>
</template>

<script>
import { mdbNavbar, mdbNavbarBrand, mdbNavItem, mdbNavbarNav, mdbNavbarToggler } from 'mdbvue'

export default {
  name: 'Header',
  components: {
    mdbNavbar,
    mdbNavbarBrand,
    mdbNavItem,
    mdbNavbarNav,
    mdbNavbarToggler,
  }
}
</script>

<style>

</style>