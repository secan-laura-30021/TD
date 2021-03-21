function run() {
  new Vue({
    el: '#app',
    data: {
      message: '',
      messageButton: ''
    },
    methods: {
      doSomething: function () {
            if( this.message == "123" ){
                this.messageButton = "123";
            }
            else{
                this.messageButton = '';
            }
      }
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  run();
});
