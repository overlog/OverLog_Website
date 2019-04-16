<template>
  <div>
    <mdb-navbar dark color="primary" position="top" transparent>
      <mdb-navbar-brand href="#" target="_blank">OVERLOG</mdb-navbar-brand>
      <mdb-navbar-toggler>
        <mdb-navbar-nav left>
          <mdb-nav-item to="/" waves-fixed>Home</mdb-nav-item>
          <mdb-nav-item href="/about" waves-fixed>About</mdb-nav-item>
          <mdb-nav-item href="/developers" waves-fixed>Developers</mdb-nav-item>
          <mdb-nav-item href="/login" waves-fixed>Login</mdb-nav-item>
          <mdb-nav-item href="/register" waves-fixed>Register</mdb-nav-item>
        </mdb-navbar-nav>
        <mdb-form-inline>
          <mdb-input type="text" placeholder="Search" aria-label="Search"/>
        </mdb-form-inline>
      </mdb-navbar-toggler>
    </mdb-navbar>
  </div>
</template>

<script>
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
  }
};
</script>

<style>
</style>