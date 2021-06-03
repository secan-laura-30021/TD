function run() {
    new Vue({
      el: '#adauga',
      data: {
        id: '',
        message: '',
        car: {}
      },
      created: function () {
      },
      methods: {
        adauga: function(){
            console.dir(this.car);

            return axios.put('http://localhost:3000/cars', this.car).then(
                (response) => {
                    this.message = response.data; // saved
                }
            );
        }
      }
    });
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    run();
  });
  