import Vue from 'vue';
import App from './App.vue';
import router from './router';
import VueI18n from 'vue-i18n';
import translations from './translations/translations';
import Buefy from 'buefy';
import axios from 'axios';
import VueAxios from 'vue-axios';

// import 'buefy/dist/buefy.css'
import 'normalize.css';
import './assets/scss/style.scss';
import 'vue2-animate/dist/vue2-animate.min.css';

import '@mdi/font/css/materialdesignicons.min.css'
import 'ionicons/dist/ionicons';

console.log(window.location.hostname);
if(window.location.hostname == 'localhost'){
  axios.defaults.baseURL = 'http://localhost:5001';
}
else{
  axios.defaults.baseURL = 'http://192.168.1.2:5001';
}

Vue.use(VueI18n);
Vue.use(Buefy);
Vue.use(VueAxios, axios)

const i18n = new VueI18n({
  locale: 'en', // set locale
  messages: translations, // set locale messages
});

Vue.config.productionTip = false

const DEFAULT_TITLE = 'Braida';

router.afterEach((to) => {

    if (to.meta && to.meta.bgImage) {
      document.body.style.backgroundRepeat = "no-repeat";
      document.body.style.backgroundPosition = "center";
      document.body.style.backgroundImage = `url(${to.meta.bgImage})`;
    } else {
      document.body.style.backgroundRepeat = "";
      document.body.style.backgroundPosition = "";
      document.body.style.backgroundImage = "";
    }
    Vue.nextTick(() => {
        document.title = i18n.t(to.meta.title) || DEFAULT_TITLE;
    });
});

new Vue({
  router,
  i18n,
  render: h => h(App),
}).$mount('#app')
