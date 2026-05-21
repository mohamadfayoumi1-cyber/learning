function submitContact(event) {
  event.preventDefault();
  const form = event.currentTarget;
  const name = form.name.value.trim();
  const email = form.email.value.trim();
  const message = form.message.value.trim();

  if (!name || !email || !message) {
    alert('Please fill in all fields before sending.');
    return;
  }

  alert(`Thanks, ${name}! Your message has been received.\nI will get back to you soon.`);
  form.reset();
}
