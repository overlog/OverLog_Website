<template>
  <div id="app">
    <Header></Header>
    <router-view/>
    <Footer class="footer"></Footer>
  </div>
</template>

<script>
import Header from "./components/Header";
import Footer from "./components/Footer";

export default {
  components: {
    Header,
    Footer
  }
};
</script>

<style>
#app {
  margin-top: 100px;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.app {
  position: absolute;
  bottom: 0;
  widows: 100%;
  height: 100;
}
</style>
