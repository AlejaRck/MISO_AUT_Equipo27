const loginFlow = {
    async typeCredentials(driver) {
      const email = "ma.pinzons1@uniandes.edu.co"; 
      const password = "Monkey2024*";

      const emailField = await driver.$('#identification');
      const passwordField = await driver.$('#password');

      await emailField.waitForDisplayed({ timeout: 5000 });
      await emailField.setValue(email);
  
      await passwordField.waitForDisplayed({ timeout: 5000 });
      await passwordField.setValue(password);
    }
  };
  
  module.exports = loginFlow;  

  