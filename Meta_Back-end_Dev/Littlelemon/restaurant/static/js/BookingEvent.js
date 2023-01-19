const date = new Date()
  document.getElementById('reservation_date').value = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate().toString().padStart(2, "0")}`
  /*  Step 10: Part two */
  document.getElementById('reservation_date').addEventListener('change', this.getBookings);
  document.getElementById('button').addEventListener( 'click', this.TakeBooking )
  // Funcs ------------------------------------+
  function TakeBooking(e) {
    e.preventDefault();
    const formdata = {
      first_name: document.getElementById('first_name').value,
      reservation_date: document.getElementById('reservation_date').value,
      reservation_slot: document.getElementById('reservation_slot').value,
    }
    fetch("{% url 'bookings' %}", { method: 'POST', body: JSON.stringify(formdata) })
      .then(r => r.text())
      .then(data => {
        getBookings()
      })
  } 
  function getBookings() {
    let reserved_slots = []
    const date = document.getElementById('reservation_date').value
    document.getElementById('today').innerHTML = date
    fetch("{% url 'bookings' %}" + '?date=' + date)
      .then(r => r.json())
      .then(data => {
        reserved_slots = []
        bookings = ''
        /* Step 11: Part three */
        data.forEach(item => {
          console.log(item.fields),
          reserved_slots.push(item.fields.reservation_slot),
          bookings += '<p>'+ item.fields.first_name + ' - ' +formatTime(item.fields.reservation_slot)+ '</p>'
        });
        /* Step 12: Part four  */
        var slot_options = '<option value="0" disabled>Select time</option>'
        for(var i = 10; i < 20; i++)
        {
          const label = formatTime(i);
          if(reserved_slots.includes(i))
          {
            slot_options += '<option value='+ i +' disabled>'+label+'</option>'
          }
          else
          {
            slot_options +=  '<option value='+ i +'>'+label+'</option>'
          }
        }
        document.getElementById('reservation_slot').innerHTML = slot_options
        if(bookings==''){
          bookings = "No bookings"
        }
        document.getElementById('bookings').innerHTML = bookings
      })
  }
  function formatTime(time) {
    const ampm = time < 12 ? 'AM' : 'PM'
    const t = time < 12 ? time : time > 12 ? time - 12 : time
    const label = `${t} ${ampm}`
    return label
  }
