export default function pastData() {
    const now = new Date();
    now.setDate(now.getDate() - 3);
    const nowFormated = `${now.getDate()}/${now.getMonth()+1}/${now.getFullYear()}`;
    console.log(nowFormated);
}