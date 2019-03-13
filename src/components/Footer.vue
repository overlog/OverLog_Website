<template>
  <mdb-navbar class="flexible-navbar white" light position="bottom" scrolling>
      <mdb-navbar-nav right>
          <mdb-nav-item href="#" waves-fixed><mdb-icon fab class="text-black" icon="facebook-square"/></mdb-nav-item>
          <mdb-nav-item href="#" waves-fixed><mdb-icon fab icon="twitter"/></mdb-nav-item>
          <mdb-nav-item href="https://github.com/overlog" waves-fixed class="border border-light rounded mr-1" target="_blank"><mdb-icon fab icon="github" class="mr-2"/>OverLOG GitHub </mdb-nav-item>
      </mdb-navbar-nav>
  </mdb-navbar>
</template>

<script>
import {mdbNavbar, mdbNavItem, mdbNavbarNav, mdbIcon} from 'mdbvue'

export default {
  name: 'Header',
  components: {
    mdbNavbar,
    mdbNavItem,
    mdbNavbarNav,
    mdbIcon
  }
}
</script>

<style scoped>

</style>