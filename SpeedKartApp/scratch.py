            # email = obj1.User.Email  # Replace `User.Email` with the actual field name
            # print("Recipient email:", email)

            # if email:
            #     try:
            #         send_mail(
            #             'User Not Available',  # Subject
            #             'The delivery agent reported the user as not available. Please contact the user to confirm the delivery.',  # Message
            #             'vishnuprasad2204@gmail.com',  # From email
            #             [email],  # Recipient list (should be a list)
            #         )
            #         messages.success(request, f'Email sent to {email}.')
            #         return redirect('Verify_otp')  # Adjust redirection as needed
            #     except Exception as e:
            #         messages.error(request, f'Failed to send email: {e}')
            # else:
            #     messages.error(request, 'Invalid email address.')
