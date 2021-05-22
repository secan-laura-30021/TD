import Vue from 'vue'
import VueRouter from 'vue-router'
import Footer from "@/views/Footer";
import PasswordChangeDone from "@/views/PasswordChangeDone";
import PasswordResetDone from "@/views/PasswordResetDone";
import EmailBoxCheckResetPassword from "@/views/EmailBoxCheckResetPassword";

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Footer',
    component: Footer
  },
  {
    path: '/shopping-cart/cart',
    name: 'Footer',
    component: Footer
  },
  {
    path: '/shopping-cart/perform-command/',
    name: 'Footer',
    component: Footer
  },
  {
    path: '/accounts/password_change/done/',
    name: 'PasswordChangeDone',
    component: PasswordChangeDone
  },
  {
    path: '/accounts/reset/done/',
    name: 'PasswordResetDone',
    component: PasswordResetDone
  },
  {
    path: '/accounts/password_reset/done',
    name: 'EmailBoxCheckResetPassword',
    component: EmailBoxCheckResetPassword
  }
]

const router = new VueRouter({
  mode: 'history',
  //base: process.env.BASE_URL,
  routes
})

export default router
