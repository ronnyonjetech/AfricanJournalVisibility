import { cn } from '@/utils/cn'
// import type { ChangeEvent, FormEvent } from 'react'
import type {  FormEvent } from 'react'
// import { useState } from 'react'



function NewsletterForm({
  className,
  onClick,
  submitText = 'Submit',
}: {
  className?: string
  onClick: (any) => void
  submitText?: string
}) {
  // const [email, setEmail] = useState('')
  // const [success, setSuccess] = useState(false)

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    // const result = await onSubmit(email)
    // console.log(result)
    // setEmail('')
    // setSuccess(true)
    console.log('mama');

  }
  function redirectToDashboard(){
    console.log('jsjsj');
    // setRedirectToDashboard(true);
    // window.location.href = '/dashboard';
  }

  // function handleChange(event: ChangeEvent<HTMLInputElement>) {
  //   setEmail(event.target.value)
   
    
  // }

  return (
    <div>
       <button
          className="-mt-px inline-flex cursor-pointer justify-center whitespace-nowrap rounded-sm border-0 bg-gradient-to-r from-secondary-500 to-secondary-400 px-7 py-4 text-center font-medium leading-4 text-white no-underline shadow-lg"
          type="submit"
        >
          dkndn
        </button>
    </div>
    // <form
    //   onSubmit={redirectToDashboard}
    //   className={cn('newsletter-form is-revealing flex flex-col gap-2 sm:flex-row', className)}
    // >
    //   {/* <div className="mr-2 flex-shrink flex-grow"> */}
    //     {/* <label className="hidden" htmlFor="email" aria-hidden="true">
    //       Email
    //     </label> */}
    //     {/* <input
    //       required
    //       placeholder="Your best email&hellip;"
    //       id="email"
    //       name="email"
    //       type="email"
    //       value={email}
    //       onChange={handleChange}
    //       autoComplete="off"
    //       className="w-full rounded-sm border border-gray-300 bg-white px-4 py-3 text-sm text-gray-500 shadow-none"
    //     /> */}
    //     {/* {success && (
    //       <div className="mt-2 text-xs italic text-gray-500">Email submitted successfully!</div>
    //     )} */}
      

    //   <div className="mr-2 flex-shrink flex-grow">
    //     <button
    //       className="-mt-px inline-flex cursor-pointer justify-center whitespace-nowrap rounded-sm border-0 bg-gradient-to-r from-secondary-500 to-secondary-400 px-7 py-4 text-center font-medium leading-4 text-white no-underline shadow-lg"
    //       type="submit"
    //     >
    //       {submitText}
    //     </button>
    //   </div>
    // </form>
    
  )
}

export default NewsletterForm